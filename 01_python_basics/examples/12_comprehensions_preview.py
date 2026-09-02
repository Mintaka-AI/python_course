"""Lesson 12: comprehension preview."""

loads_kn = [12.5, 14.0, 11.8]
loads_n = [load_kn * 1_000 for load_kn in loads_kn]
high_loads_kn = [load_kn for load_kn in loads_kn if load_kn >= 12]
rounded_loads_kn = {round(load_kn) for load_kn in loads_kn}
load_labels = {f"L-{index + 1}": load_kn for index, load_kn in enumerate(loads_kn)}

print(loads_n)
print(high_loads_kn)
print(rounded_loads_kn)
print(load_labels)
