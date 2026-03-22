# Polymorphism
# have many forms
# 2 ways to achieve polymorphism poly-many morph-many
# 1. Inheritance = an object could be treated of the same type as a parent class
# 2. "Duck typing" = Object must have necessary attributes/methods

# from abc import ABC, abstractmethod
# class Shape:
#     @abstractmethod
#     def area(self):#lets define this as abstract method
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14*self.radius **2
#
# class Rectangle(Shape):
#     def __init__(self, width, height ):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width*self.height
#
# class Triangle(Shape):
#     def __init__(self, base, side):
#         self.base = base
#         self.side = side
#     def area(self):
#         return self.base*self.side*0.5
#
# class Square(Shape):
#     def __init__(self,side):
#         self.side = side
#
#     def area(self):
#         return self.side*self.side

# circle = Circle()
# rectangle = Rectangle()
# triangle = Triangle()
# square = Square()

################ has 3 forms -->considered as pizza, circle, shape
# class Pizza(Circle):
#     def __init__(self,topping,radius):
#         # self.radius = radius
#         super().__init__(radius)
#         self.topping = topping
#
#     # def area(self):
#     #     return self.radius*self.radius
#
# shapes = [Circle(4), Rectangle(5,4), Triangle(6,7), Square(2), Pizza("pepperoni", 15)]
#
# for shape in shapes:
#     print(shape.area())

################################# Duck Typing #################################

# Duck typing = anothr wat to aachieve polymorphism besides inheritance
#             Object must have the minimum necessary attributes/methods
#             "If it looks like a duck and quacks like a duck, it must be a duck"
# as long as obj resembles another its polymorph

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("I am dog.")

class Cat(Animal):
    def speak(self):
        print("I am cat.")

class Car:
    alive = False
    def speak(self):
        print("Honk!")


animals = [Dog(),Cat(), Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)