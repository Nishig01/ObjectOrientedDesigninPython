
#
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age=age
#         self.grade=grade
#
#     def get_grade(self):
#         return self.grade
#
# class Course:
#     def __init__(self,name,max_students):
#         self.name=name
#         self.max_students = max_students
#         self.students=[]
#
#     def add_student(self,student):
#         if len(self.students)<=self.max_students:
#             self.students.append(student)
#             return True
#         return False
#
#     def get_average_grade(self):
#         val=0
#         for student in self.students:
#             val+=student.get_grade()
#         return val/len(self.students)

# s1=Student("John",45,39)
# s2=Student("Jane",45,40)
# s3=Student("Jack",55,40)
#
# course = Course("Math",2)
# course.add_student(s1)
# course.add_student(s2)
# course.add_student(s3)
# # print(course.students[0].age)
# print(course.add_student(s3))
# print(course.get_average_grade())



# Inheritance

# class Pet:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(f"I am {self.name}, {self.age} years old")
#     def speak(self):
#         print("I don't know how to speak")
#
# class Dog(Pet):
#     def speak(self):#overrides parent class method
#         print("Bark")
#
# class Cat(Pet):
#     def __init__(self,name,age,color):
#         #     initializations inherited
#         super().__init__(name,age) #method we call __init__, parameters we pass ro rhat method name and age
#         self.color=color
#     def speak(self):
#         print("Meow")
#     def show(self):
#         print(f"I am {self.name}, {self.age} years old and I am {self.color}")
#
# p=Pet("Doggy",2)
# p.show()
# c=Cat("manu",2, "brown")
# c.show()




# Class Attributes -->attributes that are specific to a class not to an instance or an object of that class
# class Person:
    # class attribute carried with the class
    # you can export
#     number_of_people=0 # will not change from instance to instance
#     GRAVITY =9.8
#     def __init__(self,name):
#         self.name=name
#         # Person.number_of_people +=1# to keep track of how many instances of Person class are created
#         Person.add_number_of_people()
#     @classmethod
#     def get_number_of_people(cls):  # not specific to instance
#         return cls.number_of_people
#     @classmethod
#     def add_number_of_people(cls): Person.number_of_people +=1
#
# p1=Person("Bob")
# p2=Person("Jim")
#
# print(p1.number_of_people)
# # Person.number_of_people+=1
# print(p2.number_of_people)
# print(p1.number_of_people)
#
# print(Person.get_number_of_people())


################################## Multiple inheritance ##################################
# Multiple inheritance-->inherit from more than one parent class C(A,B)
# Multi level inheritance -->inherit from a parent which inherits from another parent C(B) <- B(A) <- A

# You only need to write super().__init__ if you want to add extra information specific to that animal. For example, if you wanted the Hawk to have a wing_span:
# class Hawk(Predator):
#     def __init__(self, name, wing_span):
#         super().__init__(name) # Runs Animal.__init__ to set the name
#         self.wing_span = wing_span # Adds the new hawk-only info

# Multi level inheritance
class Animals:   #Prey and Predators whose parent is Animal ,are parents for Rabbits and Fish  and Hawk
    def __init__(self, name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating")
    def drink(self):
        print("drink")

class Prey(Animals):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animals):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Fish(Prey, Predator):#Multiple inheritance
    pass

class Hawk(Predator):
    pass

rabbit=Rabbit("rabu")
hawk=Hawk("hawk")
fish=Fish("mowds")

fish.flee()

