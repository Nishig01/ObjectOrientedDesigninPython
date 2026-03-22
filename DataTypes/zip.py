# zip() = Combines multiple iterables (llists, tuples, sets, dict)
#           into a single iterator.
#           Makes managing multiple indices easier

names = ["Spongebob", "Patrick", "Squidward"]
ages = [24, 25, 26]

for i in range(len(names)):
    name =names[i]
    age = ages[i] #managing differnet multiple indices is complex
    print(name, age)
    # instead we could zip fn to combine more iterables together


data = zip(names, ages)
print(data) #this is an object <zip object at 0x1034dff00>
data = list(zip(names, ages))
print(data) #list of tuples --> [('Spongebob', 24), ('Patrick', 25), ('Squidward', 26)]

data = tuple(zip(names, ages))
print(data) #(('Spongebob', 24), ('Patrick', 25), ('Squidward', 26))

data = dict(zip(names, ages))
print(data) #{'Spongebob': 24, 'Patrick': 25, 'Squidward': 26}

for names, age in data:
    print(f"{name} is {age} years old")