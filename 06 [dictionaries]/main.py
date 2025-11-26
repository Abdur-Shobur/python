# Dictionary
person = {
    "name": "Abdur",
    "age": 25
}


# print(person['name'])

# 2. Adding & Updating Items
person['city'] = "Dhaka"


# 3. Removing Items
person.pop('city')

# 4. Dictionary Methods
print(person.keys())
print(person.values())
print(person.items())


# 5. Looping Through Dictionary
for key, value in person.items():
    print(key, ":", value)


# 6. Nested Dictionaries
people = {
    "person1": {"name": "Shobur", "age": 21},
    "person2": {"name": "Rana", "age": 22}
}

print(people['person1']["age"])
