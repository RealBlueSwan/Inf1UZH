from geometric_object import GeometricObject
from math import pi


class Cone(GeometricObject):
    def __init__(self, color:str, filled:bool, radius:float, vertical_height:float, slant_height:float):
        super().__init__(color, filled)
        self.radius = radius
        self.vertical_height = vertical_height
        self.slant_height = slant_height

    def area(self) -> float:
        return  round(pi * self.radius**2 + pi * self.radius * self.slant_height, 2)

    def volume(self) -> float:
        return  round(pi * self.vertical_height * (self.radius**2) / 3, 2)
