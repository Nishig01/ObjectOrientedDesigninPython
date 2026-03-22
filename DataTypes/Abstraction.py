# Abstract class : A class that cannot be instantiated on its own; Meant to be sub-classsed.
#                   They can contain abstract methods, which are declared but have no implementation.
#                   Abstract classes benefits:
#                   1. Prevents instantiation of the class itself(incomplete like just chasis of vehicle)
#                   2. Requires children to use inherited abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# vehicle = Vehicle() #TypeError: Can't instantiate abstract class Vehicle without an implementation for abstract methods 'go', 'stop'
# vehicle.go()
# vehicle.stop()

class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("You stop the car")

class Truck(Vehicle):
    def go(self):
        print("You drive the truck")
    def stop(self):
        print("You stop the truck")

class Boat(Vehicle):
    def go(self):
        print("You sail the boat")
#   if not method implemented  --> TypeError: Can't instantiate abstract class Boat without an implementation for abstract method 'stop'

    def stop(self):
        print("You anchor the boat")

boat = Boat()

