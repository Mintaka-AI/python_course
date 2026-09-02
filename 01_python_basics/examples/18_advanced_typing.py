"""Lesson 18: type hints describe the shape of engineering data."""

from typing import Protocol, TypedDict, TypeVar


class SensorRecord(TypedDict):
    sensor_id: str
    temperature_c: float


class HasMass(Protocol):
    mass_kg: float


T = TypeVar("T")


def first_reading(values: list[T]) -> T:
    """Return the first item while preserving its type."""
    if not values:
        raise ValueError("values must contain at least one item")
    return values[0]


def total_mass(items: list[HasMass]) -> float:
    return sum(item.mass_kg for item in items)


class SteelPlate:
    def __init__(self, mass_kg: float) -> None:
        self.mass_kg = mass_kg


readings: list[SensorRecord] = [
    {"sensor_id": "T-01", "temperature_c": 21.5},
    {"sensor_id": "T-02", "temperature_c": 22.0},
]
plate = SteelPlate(12.5)

print(first_reading(readings)["sensor_id"])
print(first_reading([10, 20, 30]))
print(f"Total mass: {total_mass([plate]):.1f} kg")
