from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape_obj):
    """
    Accepts any object that 'quacks' like a Shape 
    (i.e., has area() and perimeter() methods).
    """
    print(f"Shape Type: {type(shape_obj).__name__}")
    print(f"Area:       {shape_obj.area():.2f}")
    print(f"Perimeter:  {shape_obj.perimeter():.2f}")
    print("-" * 30)


if __name__ == "__main__":

    my_circle = Circle(radius=5)
    my_rectangle = Rectangle(width=4, height=7)

    shape_info(my_circle)
    shape_info(my_rectangle)
