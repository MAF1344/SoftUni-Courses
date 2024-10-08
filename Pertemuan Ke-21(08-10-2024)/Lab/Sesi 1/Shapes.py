from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def calculate_perimeter(self):
        return 2 * pi * self._radius

    def calculate_area(self):
        return pi * self._radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def calculate_perimeter(self):
        return 2 * (self._width + self._height)

    def calculate_area(self):
        return self._width * self._height

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
print()
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

