# vessel_proximity
# Assignment

 Vessel Proximity Detection

This project is a Python-based application that detects proximity events between vessels using geographic coordinates. The goal is to identify and visualize when two vessels are within a specified distance of each other.

Project Overview

The project uses a dataset of vessel positions (`sample_data.csv`) and calculates the great-circle distance between vessels at the same timestamp. Proximity events are identified based on a user-defined threshold distance. The results are then visualized on a map using Plotly.

Features

  Proximity Detection: Calculates the distance between each pair of vessels and identifies proximity events.
  Great-Circle Distance Calculation**: Uses the Haversine formula for accurate distance calculation on a spherical Earth.
  Spatial Visualization: Visualizes the proximity events on an interactive world map.

Installation

Prerequisites

- Python 3.x
- pip (Python package installer)

Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/vessel-proximity-detection.git
   cd vessel-proximity-detection
   ```

2. Install required packages:

   Install the necessary Python packages using the provided `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

Running the Project

1. Ensure the dataset is available:
   - The dataset `sample_data.csv` should be placed in the same directory as the Python script.

2. Run the Python script:

   Execute the main script to detect proximity events and visualize the results:

   ```bash
   python vessel_proximity.py
   ```

3. Output:
   The script will print the execution time and display an interactive map showing the proximity events between vessels.

Dataset

sample_data.csv: A CSV file containing the vessel data with the following columns:
   `mmsi`: The unique identifier for each vessel.
   `timestamp`: The timestamp of the vessel's position.
   `latitude`: The latitude of the vessel's position.
   `longitude`: The longitude of the vessel's position.

How It Works

1. Data Loading:
   The script reads the vessel data from `sample_data.csv` into a Pandas DataFrame.

2. Proximity Detection:
   The Haversine formula is used to calculate the great-circle distance between every pair of vessels at the same timestamp.
   Proximity events are identified where the distance between vessels is less than the specified threshold (e.g., 1 km).

3. Visualization:
   The proximity events are visualized on an interactive world map using Plotly's `scatter_geo` function.

Performance

The script includes a timing function to measure the performance of the proximity detection process.

License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to modify this `README.md` as per your project specifics!
