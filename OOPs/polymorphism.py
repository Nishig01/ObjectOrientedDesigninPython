from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self)->float:
        pass

    @abstractmethod
    def perimeter(self)->float:
        pass

class Circle(Shape):
    def __init__(self, radius:float):
        self.radius = radius
    def area(self):
        return 3.14159*self.radius**2
    def perimeter(self):
        return 2*3.14159*self.radius

class Rectangle(Shape):
    def __init__(self, length:float, width:float):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
    def perimeter(self):
        return self.length + self.width

# rec = Rectangle(10,20)
# print(rec.area())

# Polymorphism in action
def print_shape_info(shape:Shape):
    print(f"Area: {shape.area(): .2f}, Perimeter: {shape.perimeter(): .2f}")

shapes = [Circle(5), Rectangle(5,7)]
for s in shapes:
    print_shape_info(s) #same function, different behavior
#     Area:  78.54, Perimeter:  31.42
#     Area:  35.00, Perimeter:  12.00


#Abstraction
