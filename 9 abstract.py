from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght

    def area(self):
        return self.width * self.lenght

react = Rectangle(10 , 6)
print(f"Area of rectangle : {react.area()}")