"""Lesson 09: functions, keyword arguments, and local scope."""

DEFAULT_WIDTH_M = 1.0


def rectangle_area_m2(length_m, width_m=DEFAULT_WIDTH_M):
    """Return a rectangle area in square metres."""
    local_area_m2 = length_m * width_m
    return local_area_m2


area_m2 = rectangle_area_m2(width_m=1.2, length_m=2.5)
print(f"Area: {area_m2:.2f} m²")
print(f"Global default width: {DEFAULT_WIDTH_M:.1f} m")
