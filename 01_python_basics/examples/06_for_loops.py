"""Lesson 06: for loops, break, continue, and loop else."""

loads_kn = [12.5, -999, 14.0, 35.0]

for load_kn in loads_kn:
    if load_kn == -999:
        continue
    if load_kn > 30:
        print("Load limit reached")
        break
    print(f"Accepted: {load_kn} kN")
else:
    print("All loads were checked")
