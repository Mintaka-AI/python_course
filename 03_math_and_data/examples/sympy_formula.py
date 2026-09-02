"""Symbolic stress formula. Requires SymPy."""
from sympy import Eq, solve, symbols

force_n, area_m2 = symbols("force_n area_m2", positive=True)
stress_limit_pa = 150_000_000
equation = Eq(force_n / area_m2, stress_limit_pa)
print("Required area expression:", solve(equation, area_m2)[0])
