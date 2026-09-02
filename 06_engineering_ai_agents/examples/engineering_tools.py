"""Deterministic tools shared by the Module 6 agent examples."""
from typing import Any, Callable


def calculate_stress(force_n: float, area_m2: float) -> dict[str, float | str]:
    """Calculate uniform axial stress and return the result in MPa."""
    if force_n < 0:
        raise ValueError("force_n must not be negative")
    if area_m2 <= 0:
        raise ValueError("area_m2 must be positive")
    return {
        "value": force_n / area_m2 / 1_000_000,
        "unit": "MPa",
        "formula": "stress = force_n / area_m2",
    }


TOOL_FUNCTIONS: dict[str, Callable[..., dict[str, Any]]] = {
    "calculate_stress": calculate_stress,
}
