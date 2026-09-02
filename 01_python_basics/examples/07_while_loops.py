"""Lesson 07: while loop with a safe stopping condition."""

target_pressure_bar = 5
pressure_bar = 0
max_steps = 10
steps = 0

while pressure_bar < target_pressure_bar and steps < max_steps:
    pressure_bar += 1
    steps += 1
    print(f"Pressure: {pressure_bar} bar")

if pressure_bar >= target_pressure_bar:
    print("Target pressure reached")
else:
    print("Stopped: maximum step count reached")
