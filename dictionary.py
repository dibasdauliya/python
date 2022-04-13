# just like objects in js

user = {'name': 'Ram', 'height': 70, 'shoe size': 10.5, 'hair': 'Black', 'eyes': 'Black'}

# get the type of thing
print(type(user))

# get the value using key from dictionary
print(user["name"])
# print(user.get("abc")) # throws error

# if there is no key that we search, .get() method will return None instead of throwing error like the above method does
print(user.get("name"))
print(user.get("abc")) # None

# get all the keys and values of the dictionary
print(user.keys())
print(user.values())

# add new data
user['address'] = "Bharatpur"
print(user)

# nesting dict in list
data = ([
    {"name": "Dibas", "address": "ABC"}, 
    {"name": "Hari", "address":  "CDE"}
    ]) 
print(data[0]["name"])

# nesting list inside dist
animal_sounds = {
   "cat": ["meow", "purr"],
   "dog": ["woof", "bark"],
   "fox": []
}
print(animal_sounds.get("cat"))

# more data 🤠
mattan = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}

chris = {'name': 'Chris', 'height': 68, 'shoe size': 10, 'hair': 'Brown', 'eyes': 'Brown'}

sarah = {'name': 'Sarah', 'height': 72, 'shoe size': 8, 'hair': 'Brown', 'eyes': 'Brown'}

people = [mattan, chris, sarah]

for person in people:
    print(person["height"])