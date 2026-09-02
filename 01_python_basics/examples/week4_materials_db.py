"""Week 4 practice: store and look up material properties."""

materials = {
    "steel": {"density_kg_m3": 7850, "yield_strength_mpa": 250},
    "aluminium": {"density_kg_m3": 2700, "yield_strength_mpa": 95},
}

selected_material = "steel"
properties = materials.get(selected_material)

if properties:
    print(f"Material: {selected_material}")
    print(f"Density: {properties['density_kg_m3']} kg/m³")
else:
    print("Material not found.")
