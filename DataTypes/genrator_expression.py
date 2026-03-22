# Generator expression = similar to a list comprehension but uses () instead of []
#                        creates a generator (iterator) that yields values one at a time
#                       no need to defn fn or use yield
#                       less flexible than a gen func and not reusable
#                       object = (expression for value in iterable)

# def count_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1

# num = int(input("Enter a number: "))

# counter = [(count for count in range(1, num+1)) ]#genrator expression
# print (counter) #[<generator object <genexpr> at 0x10268d900>]

# counter = (count for count in range(1, num+1))
# for n in counter:
#     print(n)


# file_path = "readable.txt"

# with open(file_path, "r") as f:
#     lines = (line.strip() for line in f)
#     for line in lines:
#         print(line)

number = int(input("Enter a numnber to sqaure up to:"))

squares = (x for x in range(1, number+1))

even_squares = (x**2 for x in range(1, number+1) if x%2==0)
for square in even_squares:
    print(square)