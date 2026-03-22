
# conditional statements---------------------------
# is_hot= True
# is_cold=True
# print(is_hot)

# if is_hot:
#     print("Its a hot day")
# elif is_cold:
#     print("Its a cold day")
# else:
#     print("Its lovely day")
# print("Enjoy your day")
#
# price1= 100000
# has_good_credit  = True
# if has_good_credit:
#     down_payment = price1*0.2
# else:
#     down_payment = price1*0.3
# print(f"Down payment: ${down_payment}")

#Logical Operator---------------------------
# And opr
# has_high_income = True
# has_good_credits = False
# has_criminal_rec = False
# if has_high_income and has_good_credits:
#     print("Eligible for loan")
# elif has_good_credits or has_high_income:
#     print("Eligible for loan but need to deposit some amount")
#
# if has_good_credits and has_high_income and not has_criminal_rec:
#     print("Eligible for signing up!")
#
# # Comparator operators---------------------------
# temperature =30
# if temperature > 30:
#     print("It's a hot day")
# elif temperature == 30:
#     print("It's a perfect day")
# else:
#     print("It's a cold day")

# Project--> Weight Convertor
# weight=input("weight:")
# unit= input("(kg)kgs or (lb)lbs:")
# if unit.upper() == "KG":
#     cw=float(weight)/0.45
#     print(f"Your weight is {cw} pounds")
# elif unit.upper() == "LB":
#     cw=float(weight)*0.45
#     print(f"You are {cw} kilos")

# While---------------------------
# i=1
# while i<=5:
#     # print(f"You are {i}  i")
#     print(i*"*")
#     i=i+1

#Project-->Guess game
# secret_number=9
# guess_count=0
# guess_limit=3
# while guess_count<=guess_limit:
#     guess = int(input("Guess number: "))
#     if guess == secret_number:
#         print("You guessed the number")
#         break #terminate loop if guessed before 3 iterations
#     guess_count=guess_count+1
# else:
#     print("You made wrong guesses")

# Game - build the car
# command =""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Sorry, you are already started")
#         else:
#             started = True
#             print("Car started..")
#     elif command == "stop":
#         if not started:
#             print("Sorry, you are stopped")
#         else:
#             started = False
#             print("Car stopped..")
#     elif command == "help":
#         print('''
# Start -to start the car
# Stop -to stop the car
# Quit -to exit the program''')
#     elif command == "quit":
#         break
#     else:
#         print("I don't know what to do")

# For---------------------------

# for item in 'Python':
#     print(item)
#
# for item in ['test', 'iterm', 'terminated']:
#     print(item)
#
# # range
# for item in range(10): # 0 to 10
#     print(item)
# for item in range(5, 10): print(item)
# for item in range(0, 10, 2): print(item)

# prices =[10,20,30]
# for price in prices:
#     if price > 10:
#         print(price)
#         break # prints only 20

# Nested loops
# (x,y)
# for x in range(4): # 0 to 3
#     for y in range(4): # 0 to 3
#         print(f'{x},{y}')

# numbers=[5,2,5,2,2]
# for number in numbers:
#     output =''
#     for i in range(number):# need this if we didn't have * multiplication of strings
#        output+='x'
#     print(output)