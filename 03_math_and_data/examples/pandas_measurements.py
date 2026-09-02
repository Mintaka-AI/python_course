"""Clean and summarize sensor data. Requires pandas."""
from pathlib import Path
import pandas as pd

path = Path(__file__).parent / "sensor_measurements.csv"
data = pd.read_csv(path)
print("Missing values:\n", data.isna().sum())
clean = data.dropna(subset=["temperature_c"])
valid = clean[clean["temperature_c"].between(-50, 150)]
print("\nSummary:\n", valid.groupby("sensor_id")["temperature_c"].agg(["count", "mean", "min", "max"]))
