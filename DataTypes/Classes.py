#Classes -->to define new types
# we studied basic types in python
# Numbers, Strings, Booleans
# Lists, Dictionaries

# Shopping cart
# functions, methods on the type

# class Point: #Capitalize first letTer of every word ->Pascal
#     def move(self):
#         print("Moving Point")
#     def draw(self):
#         print("draw Point")
#     Apart from methods these objects can also have attributes
# these attributes are like variables that belong to a particular object

# so with class we defined new type
# and we this class we can define new objects--> Instances of class
# we can store object in a variable
#
# point1= Point()
# point1.move()
# point1.x=20
# print(point1.x)

# point2 = Point()
# print(point2.x) doesnt have attribute called x


############Constructors ##################################################
# class Circle:
#     # Constructor
#     def __init__(self,x,y):   #self -->reference to current object
#         self.x=x
#         self.y=y

# when we create new Circle object Self references that object in the memory
# C1 = Circle(10,20)
#
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def agee(self, age):
#         print(f"Hi, I am {self.age} printed from class Person through constructor")
#         print(f"Hi, I am {age} printed directly")
#
# # Each object below is different instance of person class
# person1=Person("NIshi",20)
# print(person1.agee(23)) #Prints None
#
# bob=Person("Bob",34)
# print(bob.agee(29))


############ Nested Classes ##################################################
# Nested class = A class defined within another class
#                 class Outer :
#                       class Inner:

# Benefits : Allows you to logically group classes that are closely related
#            Encapsulates private details tha aren't relevant outside of the outer class
#            Keeps the namespace clean; reduces the possibility of naming conflicts

# class Employee:
#     print("This is the first class")
#
# class Employee:
#     print("This is the second class")

# Instead use nested class
class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position= position

        def get_details(self):
            return f"{self.name} {self.position}"
        # print("This is the first class")

    def __init__(self,company_name):
        self.company_name = company_name
        self.employees =[]

    def add_employees(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]


company = Company("Byteswap")
company.add_employees("Nishi", "Manager")
company.add_employees("Dhanu", "CEO")
print(company.list_employees())
for employee in company.list_employees():
    print(employee)

class Nonprofit:
    class Employee:
        print("This is the ssecond class")



# Inheritance--------------------------------------------------
# mechanism to Reusing code
# class Dog:
#     def walk(self):
#         print("I am walking")
#
# class Cat:
#     def walk(self):
#         print("I am walking")
#
# How to inherit
# class Mammal:
#     def walk(self):
#         print("I am walking")
#
# class Dog(Mammal):
#     # pass #python don't like empty classes
#     def bark(self):
#         print("I am barking")
# class Cat(Mammal):
#     pass
#
# dog1 = Dog().walk()

