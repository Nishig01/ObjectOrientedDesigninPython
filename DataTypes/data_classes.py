#Data Class = a special kind of class that's designed for holding data
            # without writing a lot of the boilerplate code for regular classes.
            # They automatically generate: __init__, __repr__,#string representation of object __eq__

from dataclasses import dataclass

# @dataclass
# class Person:
#     name: str
#     age: int
#     is_alive :bool = True
#
#
#
# person1 = Person("Spongebob", 30)
# person2 = Person("Bob", 40)
# print(person1) #when you print the object it automatically calls __repr__ method
# print(person2)
#
# print(person1 == person2) #uses __eq__ behind the sceens

# __post_init__

# @dataclass
# class Persona:
#     name: str
#     age: int
#     is_alive = True
#
#     def __post_init__(self):
#         if self.age <0:
#             raise ValueError("age cannot be negative")
#
# persona1 = Persona("John", -40)
# print(persona1.name) #ValueError: age cannot be negative

#if you want your objects to be immutable  you could add after the decorator @dataclass (frozen =True)
# @dataclass (frozen = True)
# class Persona:
#     name: str
#     age: int
#     is_alive = True
#
#     def __post_init__(self):
#         if self.age <0:
#             raise ValueError("age cannot be negative")
#
# persona1 = Persona("John", 40)
# # persona1.name = "df"  #dataclasses.FrozenInstanceError: cannot assign to field 'name'
# print(persona1.name)


#Hiding attributes
from dataclasses import field
@dataclass
class Persona:
    name: str #type hints are mandatory for dataclasses
    age: int
    password: str = field(repr = False)
    is_alive :bool = True

    def __post_init__(self):
        if self.age <0:
            raise ValueError("age cannot be negative")

persona1 = Persona("John", 40,"edrfg")
print(persona1)
