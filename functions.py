# input('x,y')
# def add(x,y):
#     return x+y
# definition declaration happens here
# while in cpp we have declaration in separate header file
# def greet_user():
#     print('Hello there!')
# greet_user()


# parameteres
# def greet_user1(name,last_name):
#     print(f'Hello {name} {last_name}')
#
# greet_user1("John","smith")#positonal arguments "John", "Smith"
# # keyword argument --->we don't have to worry about the position of the arguments
# greet_user1("Nishi", last_name="Manya")

# def calc_cost(total=50, shipping=5, discount=0.1):
#     print(total)
# calc_cost(total=50,shipping=5,discount=0.1)#keyword argument only after positional argument

# return statement
# def square(num):
#     return num*num
# print(square(4))

# def squareReturnsNone(num):#By default functions in python returns None
#      num*num
# print(squareReturnsNone(4))




# Reusable functions
# def emoji_converter(msg):
#     words = msg.split(" ")
#     # print(words) #['good', 'morning', '']
#     emojis = {
#         ":)": "😍",
#         ":/": " 😕"
#     }
#     output=" "
#     for word in words :
#         output += emojis.get(word,word)+" "
#     return output
#
# msg=input(">")
# print(emoji_converter(msg))


# Expectations
# Handling errors
# age=int(input('Age'))#exit code 1 if input other than integer
# print(age)

# try:
#     age = int(input('Age'))  # exit code 1 if input other than integer
#     print(age)
# except ValueError:
#     print('Please enter a valid age')

try:
    age=int(input("Enter your age:"))
    income=2000
    risk=income/age
    print(risk)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:#if we input 0 we still get ZeroDivisionError: division by zero !!! ValuError just checks for value type
    print("Invalid input")

# Comments
