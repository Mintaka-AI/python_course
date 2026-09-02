"""Module 2 examples: files, validation, modules, types, and JSON.

Run from the MSYS2 UCRT64 terminal:
    cd 02_engineering_code/examples
    python examples.py
"""

import csv
import json
from pathlib import Path

from calculations import calculate_stress_pa, rectangle_area_m2


EXAMPLES_DIR = Path(__file__).parent
MEASUREMENTS_PATH = EXAMPLES_DIR / "measurements.csv"


def load_measurements(path: Path) -> list[dict[str, float]]:
    """Read measurement rows from a CSV file."""
    measurements = []

    with path.open(newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            measurements.append(
                {
                    "test_id": float(row["test_id"]),
                    "load_kn": float(row["load_kn"]),
                    "area_m2": float(row["area_m2"]),
                }
            )

    return measurements


def main() -> None:
    """Run each Module 2 example."""
    print("1. Validated function with type hints")
    area_m2 = rectangle_area_m2(2.5, 1.2)
    print(f"Rectangle area: {area_m2:.2f} m²")
    print()

    print("2. Load measurements from a CSV file")
    try:
        measurements = load_measurements(MEASUREMENTS_PATH)
    except FileNotFoundError:
        print(f"Cannot find: {MEASUREMENTS_PATH}")
        return

    results = []
    for measurement in measurements:
        force_n = measurement["load_kn"] * 1_000
        stress_pa = calculate_stress_pa(force_n, measurement["area_m2"])
        result = {
            "test_id": int(measurement["test_id"]),
            "stress_mpa": round(stress_pa / 1_000_000, 2),
        }
        results.append(result)
        print(f"Test {result['test_id']}: {result['stress_mpa']} MPa")
    print()

    print("3. Convert a calculation result to JSON")
    print(json.dumps({"results": results}, indent=2))
    print()

    print("4. Handle invalid input clearly")
    try:
        calculate_stress_pa(1_200, 0)
    except ValueError as error:
        print(f"Cannot calculate stress: {error}")


if __name__ == "__main__":
    main()
