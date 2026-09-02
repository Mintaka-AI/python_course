"""Lesson 14: lambda expressions and higher-order functions."""

temperatures_c = [-3.0, 5.0, 18.0]
temperatures_f = list(map(lambda temp_c: temp_c * 9 / 5 + 32, temperatures_c))
safe_temperatures_c = list(filter(lambda temp_c: 0 <= temp_c <= 40, temperatures_c))

tests = [
    {"id": "T-1", "error_mm": 0.8},
    {"id": "T-2", "error_mm": 0.2},
    {"id": "T-3", "error_mm": 0.5},
]
tests_by_error = sorted(tests, key=lambda test: test["error_mm"])

print("Temperatures in Fahrenheit:", temperatures_f)
print("Safe temperatures:", safe_temperatures_c)
print("Tests by error:", [test["id"] for test in tests_by_error])
