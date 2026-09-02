"""Week 4 practice: reusable shape-area functions."""


def rectangle_area_m2(length_m, width_m):
    return length_m * width_m


def circle_area_m2(radius_m):
    return 3.14159 * radius_m**2


def triangle_area_m2(base_m, height_m):
    return base_m * height_m / 2


print(f"Rectangle: {rectangle_area_m2(2, 3):.2f} m²")
print(f"Circle: {circle_area_m2(1):.2f} m²")
print(f"Triangle: {triangle_area_m2(2, 3):.2f} m²")
