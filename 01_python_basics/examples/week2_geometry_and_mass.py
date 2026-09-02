"""Week 2 practice: area, volume, and mass."""

length_m = 2.0
width_m = 1.0
height_m = 0.5
density_kg_m3 = 7850

area_m2 = length_m * width_m
volume_m3 = area_m2 * height_m
mass_kg = volume_m3 * density_kg_m3

print(f"Area: {area_m2:.2f} m²")
print(f"Volume: {volume_m3:.2f} m³")
print(f"Mass: {mass_kg:.1f} kg")
