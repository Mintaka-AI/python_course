"""Lesson 02: variables, types, and casting."""

force_text = "1200"
force_n = float(force_text)
is_safe = force_n < 2_000

print(f"Force: {force_n:.1f} N")
print(f"Type: {type(force_n).__name__}")
print(f"Safe: {is_safe}")
