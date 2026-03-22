# recursion = a fn that calls itself from within

# Iterative
def walk(steps):
    for step in range(1, steps+1):
        print(f"You take step #{step}")

walk(5)

def walk1(steps):
    if steps == 0:
        return
    print(f"You take step #{steps}")
    walk1(steps-1)


walk1(6)

def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial(9))

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))

for i in range(9):
    print(fibonacci(i), end=" ") # 0 1 1 2 3 5 8 13 21