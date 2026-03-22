#exception ==> an event that interrupts the flow of a program
# (ZeroDivisorError, TypeError, ValueError)
# 1. try, 2. except, 3. finally

# 1/0 #ZeroDivisionError: division by zero

# 1+ '1' #TypeError: unsupported operand type(s) for +: 'int' and 'str'

# number = int(input("Enter a number: "))
# print(1/number)
# Enter a number: pizza
# ValueError: invalid literal for int() with base 10: 'pizza'


try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only no's plz")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup")
