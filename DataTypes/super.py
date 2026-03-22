# super() -> function used in a child class to call methods from a parent class (superclass)
#              allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.filled} and {'filled' if self.filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):  #METHOD OVERRIDING
        print(f"It is circle of {3.14*self.radius*self.radius}")
        #         you also want to use parent method
        # extend the functionality of describe method
        super().describe()

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

circle = Circle("red", False, 5)
square = Square("blue", True, 5)

print(circle.color)

circle.describe() #Because we used super