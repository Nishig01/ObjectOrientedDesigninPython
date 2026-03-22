#Single Responsibility
# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
# class UserRepository:
#     def save(self, user:User):
#         print(f"saving user {user.name}")
#         return user
#
# class EmailService:
#     def send(self, to:str, msg:str):
#         print(f"saving email {to} to {msg}")
#
# user1 = User("Nishi", "nishi@gmail.com")
# repo = UserRepository()
# email_svc = EmailService()
#
# repo.save(user1)
# email_svc.send(to="danny@gmail.com", msg="hello")

# Open for extension, Close for modification
from abc import ABC, abstractmethod
class Discount(ABC):
    @abstractmethod
    def calculate(self, price:float)->float:pass

class PercentDiscount(Discount):
    def __init__(self, percent:float):
        self.percent = percent
    def calculate(self, price:float)->float:
        return price*(1-self.percent/100)


class FlatDiscount(Discount):
    def __init__(self, flat_amount:float):
        self.flat_amount = flat_amount

    def calculate(self,  price: float)->float:
        return max(0, price - self.flat_amount)#n Python, max(0, 5.5) works perfectly fine even if one is an int and the other is a float.

disc_price = PercentDiscount(10) #percent = 10
print(disc_price.calculate(100)) # price = 100

flat_disc_price = FlatDiscount(5.5)
print(flat_disc_price.calculate(100)) #94.5

# Add new discount types without modifying existing code!

# L --> Liskov Substitution
# Any subclass should be usable where parent is expected
class Bird:
    def fly(self): return "Flying"

class Penguin(Bird):
    def fly(self): return "Penguin"

# I --> Interface Segregation
#BAD: Fat Interface

#GOOD: Small, focused interfaces
class Coder(ABC):
    @abstractmethod
    def code(self): pass

class Manager(ABC):
    @abstractmethod
    def manage(self): pass

class Developer(ABC):
    @abstractmethod
    def developer(self): pass

#D - Dependency Inversion
#BAD : High-level depends on low-level

# class MySQLDatabase:
#   def query(self, sql): ...
# class BadApp:
#   def __init__(self):
#       self.db = MySQLDatabase() # Tightly coupled!

#GOOD: Depends on abstractions
class Database(ABC):
    @abstractmethod
    def query(self, sql): pass

class GoodApp:
    def __init__(self, db:Database): #dependency injection
        self.db = db
