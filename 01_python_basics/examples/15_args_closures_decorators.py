"""Lesson 15: flexible arguments, closures, and decorators."""


def total_load(*loads_n, **metadata):
    """Return a total while accepting optional descriptive metadata."""
    print("Test:", metadata.get("test_id", "unknown"))
    return sum(loads_n)


def make_calibrator(offset_c):
    """Return a function that remembers its calibration offset."""
    def calibrate(raw_c):
        return raw_c + offset_c

    return calibrate


def announce(function):
    """Print messages around a calculation."""
    def wrapper(*args, **kwargs):
        print("Calculation started")
        result = function(*args, **kwargs)
        print("Calculation finished")
        return result

    return wrapper


@announce
def rectangle_area_m2(width_m, height_m):
    return width_m * height_m


print("Total load:", total_load(1_200, 800, 950, test_id="B-17"), "N")
calibrate_lab_a = make_calibrator(0.3)
print("Calibrated temperature:", calibrate_lab_a(20.0), "°C")
print("Area:", rectangle_area_m2(3.0, 2.0), "m²")
