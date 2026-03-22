# Sorting in python: .sort() or sorted()
# Lists[], Tuples(), Dictionaries{"":""), Objects

# -------------- Lists -----------------------
fruits = ["apple", "banana", "mango", "cherry"]
fruits.sort()
fruits.sort(reverse=True)
print(fruits)

# -------------- Tuples ------------------------

fruits1=("apple", "banana", "mango", "cherry")
fruits1 = sorted(fruits1)#gives list
fruits1 = tuple(sorted(fruits1))# converted to tuple
print(fruits1)


# ****************** Dictionaries ************************

fruits8 = {"banana": 105,
          "orange": 101,
          "apple": 102,
          "pear": 103,
          }

fruits3 = sorted(fruits8)
print(fruits3) # ['apple', 'banana', 'orange', 'pear']

fruits5 = sorted(fruits8.items()) #lsit of tuples
print(fruits5) # [('apple', 102), ('banana', 105), ('orange', 101), ('pear', 103)]

fruits6 = dict(sorted(fruits8.items()))
print(fruits6) #{'apple': 102, 'banana': 105, 'orange': 101, 'pear': 103}

# sort by key in reverse
fruits10 =dict(sorted(fruits8.items(), key = lambda item:item[0], reverse = True))
print(fruits10) # {'pear': 103, 'orange': 101, 'banana': 105, 'apple': 102}

fruits11 =dict(sorted(fruits8.items(), key = lambda item:item[1], reverse = True))
print(fruits11) #{'banana': 105, 'pear': 103, 'apple': 102, 'orange': 101}


#---------------------------Objects-----------------------------

# __repr__ create string representation of that object


class Fruits:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"Fruit-({self.name}, {self.calories})"

fruitss = [Fruits("banana", 105),
          Fruits("orange", 72),
          Fruits("pear", 73),
          Fruits("apple", 80),
          Fruits("cherry", 90)
          ]

fruitss = sorted(fruitss, key = lambda fruit:fruit.name)
print(fruitss)# [Fruit-(apple, 80), Fruit-(banana, 105), Fruit-(cherry, 90), Fruit-(orange, 72), Fruit-(pear, 73)]

fruitss1 = sorted(fruitss, key = lambda fruit:fruit.name, reverse = True)
print(fruitss1) #[Fruit-(pear, 73), Fruit-(orange, 72), Fruit-(cherry, 90), Fruit-(banana, 105), Fruit-(apple, 80)]
