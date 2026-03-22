# A Singleton is a design pattern that
# ensures a class has only one instance throughout the entire lifecycle of the program
# and provides a global point of access to it.
# It is commonly used for things like Database Connections, Logging, or Configuration settings
# where having multiple instances would waste resources or cause conflicts.

# The __new__ Approach (The Constructor Way)
# In Python, __new__ is the method responsible for actually creating a new object (whereas __init__ only initializes it).

#Working -->
# Every time you try to create a new object using s1 = Singleton(),
# Python calls __new__.
# Your code checks if _instance is empty.
# If it is, it creates it; otherwise, it just returns the one that already exists.
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # Create the object only if it doesn't exist yet
            cls._instance = super().__new__(cls)
        return cls._instance

# Pythonic way
# 2. The get_instance Approach (The Factory Way)
# This is a more explicit way of fetching the instance,
# often seen in languages like Java or C++, but also used in Python for clarity.
class DatabaseConnection:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


# How it works: Instead of calling DatabaseConnection(),
# the user calls DatabaseConnection.get_instance().
# This makes it very obvious to other developers that
# they are working with a Singleton.

class PostgresConnection(DatabaseConnection):
    pass

conn1 = DatabaseConnection.get_instance()
conn2 = PostgresConnection.get_instance()

print(conn1 == conn2) #True
# Why? -->_instance is defined on DatabaseConnection,
# and subclasses share that same class variable

# To get separate instance per class
class DataBaseCon:
    _instance = None

    @classmethod
    def get_instance(cls):
        if not hasattr(cls, '_own_instance') or cls._own_instance is None:
            cls._own_instance = cls()
        return cls._own_instance

class DataBaseConn:
    _instances = {}

    @classmethod
    def get_instance(cls):
        if cls not in cls._instances:
            cls._instances[cls] = cls()
        return cls._instances[cls]

class PostgresConn(DataBaseConn):
    pass
db = DataBaseConn.get_instance()
pg = PostgresConn.get_instance()
print(db == pg) #False
