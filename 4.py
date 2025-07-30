from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def area(self):
        return self.width * self.heigth


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())
print(round(circle.area(), 2))
