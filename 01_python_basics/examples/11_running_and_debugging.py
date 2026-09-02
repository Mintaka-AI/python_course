"""Lesson 11: use clear values to make debugging easier."""

force_n = 1_200
area_m2 = 0.02

print(f"DEBUG force_n={force_n}, area_m2={area_m2}")
stress_pa = force_n / area_m2
print(f"Stress: {stress_pa:.0f} Pa")
