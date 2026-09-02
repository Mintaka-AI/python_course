"""Lesson 03: arithmetic, comparison, and assignment operators."""

force_n = 1_200
area_m2 = 0.02
stress_pa = force_n / area_m2
force_n += 300

print(f"Stress: {stress_pa:.0f} Pa")
print(f"Updated force: {force_n} N")
print(f"Within limit: {stress_pa <= 100_000}")
