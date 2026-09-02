"""Dimensional-check example. Requires Pint."""
from pint import UnitRegistry

units = UnitRegistry()
force = 12.5 * units.kilonewton
area = 800 * units.millimeter**2
stress = (force / area).to("megapascal")
print(f"Stress: {stress:.3f}")
