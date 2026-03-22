# vectors -- arrays                                   list []      vector<vector> [ [], [] ]
# strings
# hashmap -> map unordered_map set unordered_set      dictionaries?
# stack queue deque
# pairs                                               tuples?
# linkedlist -->class or struct
# heaps


# Tuples
# similar to lists
# we cannot modify them --> we cant add new items we cant remove items , pop, insert not available
# they are IMMUTABLE

# Can only get information of tuple
# magic methods __
# count and index
numbers=(1,2,3,4,5)
numbers.count(1)
print(numbers[0])

# Unpacking--------------------------
coordinates = (1,2,3)
x1=coordinates[0]
y1=coordinates[1]
z1=coordinates[2]

# unpacking
x,y,z = coordinates
print(x,y,z)

