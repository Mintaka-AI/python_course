"""Lesson 27: handle an expected conversion error."""

pressure_text = "not-a-number"

try:
    pressure_bar = float(pressure_text)
except ValueError:
    print("Pressure must be a number, for example 2.5.")
else:
    print(f"Pressure: {pressure_bar} bar")
finally:
    print("Input check complete.")
