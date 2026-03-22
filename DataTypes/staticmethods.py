# STATIC METHOD
# you want to create classes that kind of organize functions together
# they do something but they don't change anything
# More organzatinoal thing

# static method--> a method that belong to a class rather than any object from that class(instance)
#                   usually used for general utility functions

# Instance methods -for operations on instances if the lass(objectS)
# Static methods - for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "cook", "CEO"]
        return position in valid_positions


print(Employee.is_valid_position("Cook"))#False  #static method you only have to access from that class you dont need to create obejct


e1 = Employee("Tim", "SE")
print(e1.get_info())



class Math:
    @staticmethod
    def add5(x):
        return 5+x

    @staticmethod
    def add6(x):
        return 6+x

    @staticmethod
    def pr():
        print('run')

print(Math.add5(5))
Math.pr()

# @staticmethod
# In Python, @staticmethod is a decorator
# used to define a method inside a class that
# does not access or modify the class state or the instance state.
# Unlike regular methods(which  take self) or
# class methods(which take cls), a static method takes no special first argument.

# class Calculator:
#     @staticmethod
#     def add(a, b):
#         return a + b
#
# # You can call it without creating an instance of the class
# print(Calculator.add(5, 10))  # Output: 15