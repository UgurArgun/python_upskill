from abstraction2 import Square, Circle, Cube, Cylinder, Shape
from day4.abstraction import square

square: Square = Square(2.5)
circle: Circle = Circle(3.5)
cube: Cube = Cube(4)
cylinder: Cylinder = Cylinder(5, 10)

print("------------------------------------------------------------")

shape: Shape = Cylinder(5, 10)
print(shape)

print("------------------------------------------------------------")

def display_area(sh: Shape):
    print(f"Area of {type(sh).__name__}: {sh.area()}")

display_area(shape)

print("------------------------------------------------------------")

shapes = [(Square(2), "Square"), (Circle(3), "Circle"), (Cube(4), "Cube"), (Cylinder(5, 10), "Cylinder")]
for shape, name in shapes:
    display_area(shape)