import pandas as pd
import numpy as np
from scipy.spatial import distance_matrix
import geopandas as gpd
import plotly.express as px
from shapely.geometry import Point
from math import radians, sin, cos, sqrt, atan2
import time

# Record the start time to measure performance
start_time = time.time()

# Load the dataset
data = pd.read_csv('sample_data.csv')

# Rename columns for easier reference
data.columns = ['mmsi', 'timestamp', 'latitude', 'longitude']

# Function to compute the great-circle distance between two points
def haversine(lon1, lat1, lon2, lat2):
    R = 6371  # Earth's radius in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Vectorized function to detect proximity events
def detect_proximity_events(data, threshold_distance):
    # Sort data by timestamp
    data = data.sort_values(by='timestamp')
    
    proximity_results = []

    # Group data by timestamp
    grouped = data.groupby('timestamp')
    
    for timestamp, group in grouped:
        coords = group[['latitude', 'longitude']].to_numpy()
        mmsis = group['mmsi'].to_numpy()
        
        # Initialize distance matrix
        dist_matrix = np.zeros((len(coords), len(coords)))
        
        # Compute distances between all pairs
        for i in range(len(coords)):
            for j in range(len(coords)):
                if i != j:
                    dist_matrix[i, j] = haversine(coords[i][1], coords[i][0], coords[j][1], coords[j][0])
        
        # Find pairs within the distance threshold
        within_threshold = dist_matrix <= threshold_distance
        close_pairs = np.where(within_threshold)
        
        seen_pairs = set()
        
        for i, j in zip(close_pairs[0], close_pairs[1]):
            if (i, j) in seen_pairs or (j, i) in seen_pairs:
                continue
            seen_pairs.add((i, j))
            mmsi1 = mmsis[i]
            mmsi2 = mmsis[j]
            if mmsi1 != mmsi2:
                proximity_results.append({
                    'mmsi1': mmsi1,
                    'mmsi2': mmsi2,
                    'timestamp': timestamp,
                    'lat1': coords[i][0],
                    'lon1': coords[i][1],
                    'lat2': coords[j][0],
                    'lon2': coords[j][1],
                    'distance': dist_matrix[i, j]
                })
    
    return pd.DataFrame(proximity_results)

# Set the distance threshold in kilometers
distance_threshold = 1.0

# Run the proximity detection
proximity_df = detect_proximity_events(data, distance_threshold)

end_time = time.time()

print(f"Execution time: {(end_time - start_time) * 1000:.2f} ms")

# Convert to GeoDataFrame for spatial plotting
gdf = gpd.GeoDataFrame(
    proximity_df,
    geometry=gpd.points_from_xy(proximity_df.lon1, proximity_df.lat1),
    crs="EPSG:4326"  # Coordinate reference system for WGS84
)

# Create a Plotly scatter plot
fig = px.scatter_geo(
    gdf,
    lon=gdf.geometry.x,
    lat=gdf.geometry.y,
    color="mmsi1",
    hover_name="mmsi2",
    title="Vessel Proximity Events",
    projection="natural earth"
)

# Display the plot
fig.show()