"""Lesson 05: conditions."""

temperature_c = 85
pressure_bar = 5

if temperature_c < 0:
    print("Below freezing")
elif temperature_c <= 80 and pressure_bar <= 10:
    print("Normal operating range")
else:
    print("Check the system")
