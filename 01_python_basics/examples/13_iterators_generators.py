"""Lesson 13: iterators and generators for sensor data."""


def calibrated_readings(raw_readings):
    """Yield one calibrated reading at a time."""
    offset_c = 0.2
    for raw_reading in raw_readings:
        yield raw_reading + offset_c


sensor_ids = ["S-01", "S-02", "S-03"]
sensor_iterator = iter(sensor_ids)
print("First sensor:", next(sensor_iterator))
print("Second sensor:", next(sensor_iterator))

raw_readings_c = [19.5, 20.1, 20.4]
print("Calibrated readings:")
for reading_c in calibrated_readings(raw_readings_c):
    print(f"{reading_c:.1f} °C")

loads_kn = [2.5, 4.0, 3.2]
loads_n = (load_kn * 1_000 for load_kn in loads_kn)
print("Total load:", sum(loads_n), "N")
