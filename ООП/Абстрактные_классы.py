from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...
    @abstractmethod
    def perimetr(self):
        ...

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2
    def perimetr(self):
        return 2 * 3.14 * self.r


c = Circle(5)
print(c.area())