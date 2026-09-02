"""Validated engineering calculation functions."""


def rectangle_area_m2(length_m: float, width_m: float) -> float:
    """Return rectangle area in square metres."""
    if length_m < 0 or width_m < 0:
        raise ValueError("Length and width must not be negative.")
    return length_m * width_m


def calculate_stress_pa(force_n: float, area_m2: float) -> float:
    """Return stress in pascals."""
    if force_n < 0:
        raise ValueError("Force must not be negative.")
    if area_m2 <= 0:
        raise ValueError("Area must be greater than zero.")
    return force_n / area_m2
