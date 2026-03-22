from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self): pass

class Dog(Animal):
    def speak(self): return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class AnimalFactory:
    @staticmethod
    def create(animal_type:str)->Animal:
        factories = {"dog": Dog, "cat": Cat}
        if animal_type not in factories:
            raise ValueError(f"Unknown: {animal_type}")
        return factories[animal_type]()
# factories: A dictionary mapping types to classes.
# [animal_type]: Accessing the value associated with that key (this returns the Class).
# (): The parentheses instantiate the class (they call the constructor).
animal = AnimalFactory.create("dog")

# Accessing a single value
# Method           Syntax               What happens if the key is missing?
# Square Brackets   my_dict["key"]      Raises a KeyError (Crashes).get()
# Method            my_dict.get("key")  Returns None (Safe)

