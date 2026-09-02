"""Lesson 08: collections and common collection functions."""

loads_kn = [12.5, 14.0, 11.8]
loads_copy = loads_kn.copy()
sensor_ids = {101, 102, 101}
limit_kn = [13.0, 13.0, 13.0]
dimensions_m = (2.5, 1.2)
material_limits_mpa = {"steel": 250, "aluminum": 150}

print(f"Maximum load: {max(loads_kn)} kN")
print(f"All below limit: {all(load <= limit for load, limit in zip(loads_kn, limit_kn))}")
print(f"Unique sensors: {sensor_ids}")
print(f"Independent list copy: {loads_copy}")
print(f"Length from tuple: {dimensions_m[0]} m")
print(f"Steel limit: {material_limits_mpa.get('steel')} MPa")
print(f"Unknown limit: {material_limits_mpa.get('titanium', 'not set')}")
for material, limit_mpa in material_limits_mpa.items():
    print(f"{material}: {limit_mpa} MPa")
