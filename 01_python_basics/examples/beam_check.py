"""Module 1 capstone: beam stress check.

Run:
    python beam_check.py

Run interactively:
    python beam_check.py --interactive
"""

import math
import sys


STRESS_LIMIT_PA = 250_000_000


def calculate_stress_pa(force_n, area_m2):
    """Return stress in pascals after validating physical inputs."""
    if not math.isfinite(force_n):
        raise ValueError("Force must be a finite number.")
    if not math.isfinite(area_m2):
        raise ValueError("Area must be a finite number.")
    if force_n < 0:
        raise ValueError("Force must not be negative.")
    if area_m2 <= 0:
        raise ValueError("Area must be greater than zero.")
    return force_n / area_m2


def read_inputs() -> tuple[float, float]:
    """Read force and area only when interactive mode was requested."""
    return float(input("Force (N): ")), float(input("Area (m²): "))


def main() -> None:
    if "--interactive" in sys.argv[1:]:
        try:
            force_n, area_m2 = read_inputs()
        except ValueError:
            raise SystemExit("Input error: enter numeric values.") from None
    else:
        force_n, area_m2 = 120_000.0, 0.0008

    try:
        stress_pa = calculate_stress_pa(force_n, area_m2)
    except ValueError as error:
        raise SystemExit(f"Input error: {error}") from error

    print(f"Stress: {stress_pa / 1_000_000:.1f} MPa")

    if stress_pa <= STRESS_LIMIT_PA:
        print("Result: stress is within the limit.")
    else:
        print("Result: stress exceeds the limit.")


if __name__ == "__main__":
    main()
