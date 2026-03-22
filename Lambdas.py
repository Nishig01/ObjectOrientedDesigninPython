#Lambda function = a small anonymous function for a one time use (throw away fn)
#                   they rake any no. of args, but have only 1 expression
#                   helps keep the namespace clean and is useful with higher order fns
#                   'sort()', 'map()', 'filter()', 'reduce()'
#                      lambda parameters : expression

# map(lambda x:x*2, numbers)
double =lambda x: x*2

print(double(2))
add = lambda x,y : x+y
print(add(2,5))

max_value =lambda x, y: x if x>y else y
print(max_value(4,8))

min_value = lambda x,y : x if x<y else y
print(min_value(4,8))

full_name =lambda first, last : f"{first} {last}"
print(full_name("Nishi","Anju"))

is_even = lambda  x: x%2 ==0
print(is_even(4))

age_check = lambda age : age>=18
print(age_check(24))