"""Week 3 practice: create a table of values."""

spring_constant_n_m = 2_000

print("Displacement (m) | Force (N)")
for displacement_mm in range(0, 26, 5):
    displacement_m = displacement_mm / 1_000
    force_n = spring_constant_n_m * displacement_m
    print(f"{displacement_m:16.3f} | {force_n:9.1f}")
