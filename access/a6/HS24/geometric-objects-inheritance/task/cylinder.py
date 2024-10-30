from geometric_object import GeometricObject
from math import pi


class Cylinder(GeometricObject):
    def __init__(self, color, filled, radius, height):
        super().__init__(color, filled)
        self.radius = radius
        self.height = height

    def area(self):
        return round(2 * pi * self.radius**2 + 2 * pi *self.radius * self.height, 2)

    def volume(self):
        return round(pi * self.height * self.radius**2, 2)
