"""Lesson 10: strings and f-strings."""

material = "  Structural Steel  "
yield_strength_mpa = 250
clean_material = material.strip()

print(clean_material.lower())
print(clean_material.replace(" ", "_"))
print(f"First letter: {clean_material[0]}")
print(f"First word: {clean_material[:10]}")
print(f"Words: {clean_material.split()}")
print(f"Joined code: {'-'.join(clean_material.split())}")
print(f"{clean_material}: {yield_strength_mpa:.0f} MPa")
