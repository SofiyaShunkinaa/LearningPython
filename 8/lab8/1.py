import abc
import math


class Shape(abc.ABC):
    @abc.abstractmethod
    def calculate_area(self): pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


circle1 = Circle(10)
print(circle1.calculate_area())
rect1 = Rectangle(5, 12)
print(rect1.calculate_area())