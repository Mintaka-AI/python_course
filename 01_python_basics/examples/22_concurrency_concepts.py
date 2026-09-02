"""Run independent simulated sensor waits without shared mutable state."""

from concurrent.futures import ThreadPoolExecutor
import time


def read_simulated_sensor(sensor_id: str) -> tuple[str, float]:
    """Simulate an I/O wait, then return one independent measurement."""
    delays_s = {"A1": 0.03, "B2": 0.01, "C3": 0.02}
    readings_c = {"A1": 20.5, "B2": 21.0, "C3": 19.8}
    time.sleep(delays_s[sensor_id])
    return sensor_id, readings_c[sensor_id]


def main() -> None:
    sensor_ids = ["A1", "B2", "C3"]
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(read_simulated_sensor, sensor_id) for sensor_id in sensor_ids]
        results = [future.result() for future in futures]

    readings_by_sensor = dict(results)
    for sensor_id in sensor_ids:
        print(f"{sensor_id}: {readings_by_sensor[sensor_id]:.1f} °C")


if __name__ == "__main__":
    main()
