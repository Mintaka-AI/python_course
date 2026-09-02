"""Lesson 19: custom exceptions and context managers."""

from contextlib import contextmanager


class InvalidPressureError(ValueError):
    """Raised when a pressure is not physically valid."""


def pressure_ratio(actual_kpa: float, limit_kpa: float) -> float:
    if actual_kpa < 0:
        raise InvalidPressureError("Pressure cannot be negative.")
    if limit_kpa <= 0:
        raise InvalidPressureError("Pressure limit must be greater than zero.")
    return actual_kpa / limit_kpa


@contextmanager
def test_section(name: str):
    print(f"Starting {name}")
    try:
        yield
    finally:
        print(f"Finished {name}")


with test_section("pressure check"):
    try:
        ratio = pressure_ratio(180.0, 250.0)
        print(f"Pressure ratio: {ratio:.2f}")
        pressure_ratio(-5.0, 250.0)
    except InvalidPressureError as error:
        print(f"Input error: {error}")
