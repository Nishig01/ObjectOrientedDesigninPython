# Lists= [] ordered and changeable . Duplicates OK
# Set={} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple =() ordered and changeable. Duplicates OK. Faster
from os import name

#################################Sets
name= {'john', 'term', 'ironman', 'jessi'}
print(dir(name))
print(help(name))
print(len(name))
print(type(name))

name.add("mango")
print(name)
print(name.remove("mango"))
print("pines" in name)
name.pop()# randomly deleted
print(name)

########################################Lists
# name= ['john', 'term', 'ironman', 'zombie']
# print(name[-1])
# print(name[2:3])#new list
from enum import unique

# Largest number in the list
# numbers=[13,4,2,6,19]
# max=numbers[0]
# print(f"length {len(numbers)}")
# for i in range(1,len(numbers)):
#     print(numbers[i], i)
#     if numbers[i] > max:
#         max=numbers[i]
# print(max)

# #2 D lists
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# # q=matrix[0][1]
# # print(q)
#
# for r in matrix:
#     for c in r:# r=[1,2,3] then r=[4,5,6] then r=[7,8,9]
#         print(c,end=" ")
#     print()
#     # print("\n")
#
# for i in range (len(matrix)): #gives i the values: 0, 1, 2.
#     for j in range (len(matrix[i])):
#         print(matrix[i][j],end=" ")

# List methods
# numbers = [5,4,3,2,7]
# numbers.append(20)# at the ned of the list
# print(numbers)
# numbers.insert(0,12) #index where it should be inserted
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# print(numbers.count(5))
# print(numbers.count(7))
# print(numbers.index(5)) #returns first occurence
# print(50 in numbers)    # is 50 in numbers?
# numbers.pop()
# numbers.remove(5)
# numbers.clear()
# print(numbers)
# nums2= numbers.copy()
# print(nums2)

# Removing duplicates in a list
# numbers = [5,5,4, 3,3,2,7]
# numbers.sort()
# i=numbers[0]
# for i in range(1,len(numbers)):#0 to len-1
#     if(numbers[i]==numbers[i-1]):
#         print(f"{numbers[i]} is the duplicate")
#
# # giving out a new list
# uniques =[]
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)



# Unpacking--------------------------
coordinates = [1,2,3]
x=coordinates[0]
y=coordinates[1]
z=coordinates[2]

# unpacking
x,y,z = coordinates
print(x,y,z)
