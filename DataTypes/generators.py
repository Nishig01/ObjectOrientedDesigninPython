# Generators = fn that behaves like an iterator (it can be used in a for loop)
#     Pauses a fn, returns a value, then resumes
#     Uses 'yeild' instead or 'return'
#     Iterate without loading everything into memery (ex. reading large files)
#      return = Poring bucket
#      yeild = drip faucet

# def count_to(n):
#     numbers = []
#     count =1
#     while count<=n:
#         # numbers.append(count)
#         yield count # pauses the fn returns the value and resume the fn again
#         count +=1
#     # return numbers # can give memory error
#
# number = int(input("Enter a number to count to:"))
#
# # for n in count_to(number):
# #     print(n)
#
# print([x for x in count_to(number)])


# def read_file(file_path):
#     with open(file_path) as f:
#         for line in f:
#             yield line.strip()
#
# file_path = "readable.txt"
# for line in read_file(file_path):
#     print(line)