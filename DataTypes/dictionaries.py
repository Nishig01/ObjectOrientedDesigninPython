# storing key value pairs

# Name: Nishi Mali
# Email: nishigandha@gmail.com
# phone: 1233

# customer = {
#     "name": "John Smoth",
#     "age":30,
#     "is_married":True
# }
# print(customer)
# customer["name"] = "nishi"
# print(customer)
# customer["age"] = 25
# print(customer)
#
# get method really useful when some key isn't there in the dictionary
# print(customer.get("name"))
# print(customer.get("nonovaluefdfsd"))#prints None
# print(customer.get("Birthday", "1st september"))#we can pass default value

# phone =input("Phone number")
# # digits_mapping={#######Error: can only concatenate str (not "int") to str#######
# #     "1":1,
# #     "2":2,
# #     "3":3,
# #     "4":4,
# # }
# digits_mapping={
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":'four',
# }
# output=""
# for ch in phone:
#     # output+=digits_mapping.get(ch, "!") ######Error: can only concatenate str (not "int") to str#######
#     output+=(digits_mapping.get(ch,"!")+ " " )
# print(output)

# Emoji convertor
msg= input(">")
words= msg.split(" ")
# print(words) #['good', 'morning', '']
emojis ={
  ":)": "😍",
    ":/":" 😕"
}

output=""
for word in words:   #dictionary.get(key, default_value)
    output+=emojis.get(word, word) +' ' # if we don't have an item with that key then we simply use that word as a default value
print(output)

# listeners = {}
# listeners.setdefault(event, [])
# The .setdefault(key, default_value) method does two things:
# Checks: Does the event (the key) already exist in self._listeners?
# Acts: * If Yes: It simply returns the value (the list) already stored there.
# If No: It creates a new entry with the event as the key and an empty list [] as the value, then returns that empty list.

