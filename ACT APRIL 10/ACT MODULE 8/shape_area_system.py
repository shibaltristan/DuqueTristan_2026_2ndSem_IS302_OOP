import math

class Shapetld:
    def area(self):
        pass

class Rectangletld(Shapetld):
    def __init__(self, widthtld, heighttld):
        self.widthtld = widthtld
        self.heighttld = heighttld

    def area(self):
        return self.widthtld * self.heighttld

class Circletld(Shapetld):
    def __init__(self, radiustld):
        self.radiustld = radiustld

    def area(self):
        return math.pi * self.radiustld * self.radiustld

class Triangletld(Shapetld):
    def __init__(self, basetld, heighttld):
        self.basetld = basetld
        self.heighttld = heighttld

    def area(self):
        return 0.5 * self.basetld * self.heighttld

# Example usage
rectangletld = Rectangletld(10, 5)
circletld = Circletld(5)
triangletld = Triangletld(8, 6)

print("Rectangle Area:", rectangletld.area())
print("Circle Area:", round(circletld.area(), 1))
print("Triangle Area:", triangletld.area())