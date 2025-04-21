class Shape:

    def area(self) -> float:
        pass

class Square(Shape):
        pass


class Circle(Shape):
        pass

square = Square()
circle = Circle()
shape = Shape()

print(square.area())
print(circle.area())
print(shape.area())

