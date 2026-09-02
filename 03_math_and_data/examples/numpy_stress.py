"""Vectorized stress calculations. Requires NumPy."""
import numpy as np

forces_n = np.array([10_000.0, 12_500.0, 15_000.0])
areas_m2 = np.array([0.0008, 0.0008, 0.0010])
stresses_mpa = forces_n / areas_m2 / 1_000_000

print("Stress values (MPa):", stresses_mpa)
print(f"Mean stress: {stresses_mpa.mean():.3f} MPa")
