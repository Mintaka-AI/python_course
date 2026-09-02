"""Run with: python -m pytest test_calculator.py"""
import pytest
from calculator import calculate_stress_pa


def test_known_stress() -> None:
    assert calculate_stress_pa(120_000, 0.0008) == 150_000_000


def test_zero_area_is_rejected() -> None:
    with pytest.raises(ValueError, match="Area must be greater than zero"):
        calculate_stress_pa(1_200, 0)
