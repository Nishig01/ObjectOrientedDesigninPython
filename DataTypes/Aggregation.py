#Aggregation --> Represents a relationship where one object (the whole)
#               contains references to one or more INDEPENDENT objects(the parts)
#               "has-a" relationship
# Composition= The composed object directly owns its components, which cannot exist independently
#                 "own-a" relationship

#################Aggregation#################
# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def list_books(self):
#         return [f"{book.title} by {book.author}" for book in self.books]
#         # lst=[]
#         # for book in self.books:
#         #     lst.append(f"{book.title} - {book.author}")
#         # return lst
#
# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
#
# library =Library("NYC library")
#/###########################################If i delete library books still exist
# book1 = Book("Harry Potter","J.K.Rowling")
# book2 = Book("The Hobbit","J. R. R. Tolkein")
#
# library.add_book(book1)
# library.add_book(book2)
# print(library.list_books())

#################Composition#################
class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, wheel_radius):
        self.wheel_radius = wheel_radius

#/###########################################If i delete Car ->Engine and Wheel don't still exist

class Car: # Car class owns some objects --> It owns an engine and 4 wheels
    def __init__(self, make, model, horse_power, wheel_radius):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_radius) for _ in range(4)] #4 wheel objects -- Composition

    def display(self):
        return f"{self.make} {self.model} {self.engine.horse_power} {self.wheels[0].wheel_radius}"

car = Car("Ford", "Mustang", 500, 18)
print(car.display())



