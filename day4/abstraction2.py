import math
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__})'

class Volume(ABC):
    @abstractmethod
    def volume(self):
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__})'

class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
       return math.pi * (self.radius ** 2)

class Cube(Shape, Volume):
    def __init__(self, side: float):
        self.side = side

    def area(self):
        return 6 * (self.side ** 2)

    def volume(self):
        return self.side ** 3

class Cylinder(Shape, Volume):
    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height

    def area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

square = Square(5)
print(square)
print(f"Area of square: {square.area()}")

circle = Circle(3)
print(circle)
print(f"Area of circle: {circle.area()}")

cube = Cube(4)
print(cube)
print(f"Area of cube: {cube.area()}")

cylinder = Cylinder(3, 5)
print(cylinder)
print(f"Area of cylinder: {cylinder.area()}")
print(f"Volume of cylinder: {cylinder.volume()}")