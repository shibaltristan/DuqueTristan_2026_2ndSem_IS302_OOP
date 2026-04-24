import math

class Shape_TLD:
    def area_TLD(self_TLD):
        pass  # Placeholder for polymorphism

class Rectangle_TLD(Shape_TLD):
    def __init__(self_TLD, width_TLD, height_TLD):
        self_TLD.width_TLD = width_TLD
        self_TLD.height_TLD = height_TLD

    def area_TLD(self_TLD):
        return self_TLD.width_TLD * self_TLD.height_TLD

class Circle_TLD(Shape_TLD):
    def __init__(self_TLD, radius_TLD):
        self_TLD.radius_TLD = radius_TLD

    def area_TLD(self_TLD):
        return math.pi * self_TLD.radius_TLD ** 2

class Triangle_TLD(Shape_TLD):
    def __init__(self_TLD, base_TLD, height_TLD):
        self_TLD.base_TLD = base_TLD
        self_TLD.height_TLD = height_TLD

    def area_TLD(self_TLD):
        return 0.5 * self_TLD.base_TLD * self_TLD.height_TLD

# Example usage
rectangle_TLD = Rectangle_TLD(10, 5)
circle_TLD = Circle_TLD(5)
triangle_TLD = Triangle_TLD(8, 6)

print(f"Rectangle Area: {rectangle_TLD.area_TLD()}")
print(f"Circle Area: {circle_TLD.area_TLD():.1f}")
print(f"Triangle Area: {triangle_TLD.area_TLD()}")
