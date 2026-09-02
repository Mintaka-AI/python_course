"""Tests for Module 2 calculation examples.

Run from this folder:
    python -m pytest
"""

import pytest

from calculations import calculate_stress_pa, rectangle_area_m2


def test_rectangle_area_m2() -> None:
    assert rectangle_area_m2(2.5, 1.2) == 3.0


def test_calculate_stress_pa() -> None:
    assert calculate_stress_pa(120_000, 0.0008) == 150_000_000


def test_stress_requires_positive_area() -> None:
    with pytest.raises(ValueError, match="Area must be greater than zero"):
        calculate_stress_pa(1_200, 0)
