"""Module 0 examples: check Python and run a first program.

Run from the MSYS2 UCRT64 terminal:
    python examples.py
"""

# Example 1: Python performs calculations.
length_m = 2.5
width_m = 1.2
area_m2 = length_m * width_m

print("Example 1: rectangle area")
print(f"Length: {length_m} m")
print(f"Width: {width_m} m")
print(f"Area: {area_m2} m²")
print()

# Example 2: Convert temperature from Celsius to Fahrenheit.
temperature_c = 25
temperature_f = temperature_c * 9 / 5 + 32

print("Example 2: temperature conversion")
print(f"{temperature_c} °C = {temperature_f} °F")
print()

# Example 3: Print a clear message for the current project.
project_name = "Engineering AI Agents"

print("Example 3: first project message")
print(f"Python is ready for {project_name}!")
