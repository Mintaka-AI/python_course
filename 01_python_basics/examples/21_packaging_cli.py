"""A standard-library command-line calculation example.

Run with defaults:
    python 21_packaging_cli.py
Run with values:
    python 21_packaging_cli.py --force 12000 --area 0.006 --material aluminum
"""

import argparse
import math


def calculate_stress(force_n: float, area_m2: float) -> float:
    """Return normal stress in pascals after checking physical inputs."""
    if not math.isfinite(force_n) or not math.isfinite(area_m2):
        raise ValueError("force and area must be finite numbers")
    if force_n < 0:
        raise ValueError("force must be zero or greater")
    if area_m2 <= 0:
        raise ValueError("area must be greater than zero")
    return force_n / area_m2


def parse_arguments() -> argparse.Namespace:
    """Read options; defaults let this teaching example run directly."""
    parser = argparse.ArgumentParser(description="Calculate normal stress.")
    parser.add_argument("--force", type=float, default=12_000.0, help="Force in N")
    parser.add_argument("--area", type=float, default=0.006, help="Area in m²")
    parser.add_argument("--material", default="steel", help="Report label")
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    try:
        stress_pa = calculate_stress(args.force, args.area)
    except ValueError as error:
        raise SystemExit(f"Input error: {error}") from error

    print(f"Material: {args.material}")
    print(f"Stress: {stress_pa:.1f} Pa")


if __name__ == "__main__":
    main()
