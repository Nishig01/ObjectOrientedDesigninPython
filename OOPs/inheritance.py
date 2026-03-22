class Animal:
    def __init__(self, name:str):
        self.name = name

    def speak(self)->str:
        raise NotImplementedError("Subclass must implement")

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"
        # self.__class__
        #This points to the class that created the specific object (instance).
        # If your object is a Car, self.__class__ points to the Car class definition itself.
    # This is a built-in attribute of any Python class that returns its name as a string.
    # If the class is Car, it returns "Car".
    # {self.name}
    # This pulls the specific value stored in that object's name attribute (e.g., "Tesla").

class Dog(Animal):
    def speak(self)->str:
        return f"{self.name} 'Woof!'"
    def fetch(self, item:str)->str:
        return f"{self.name} fetches {item}"

class Cat(Animal):
    def speak(self)->str:
        return f"{self.name} 'Meow!"

            #  Multiple Inheritance
class DogCat(Dog, Cat):
    def speak(self)->str:
        return f"{Dog.speak(self)} and {Cat.speak(self)}"

dog = Dog("dogesh")
print(dog.speak())
cat = Cat("cat")
print(cat.speak())
print(DogCat.mro())
# Children before parents: DogCat always comes before Dog and Cat.
# Left-to-right: Since you wrote (Dog, Cat), Dog is checked before Cat.
# No duplicates: Each class appears only once in the list.





