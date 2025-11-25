# Data type Conversion

x = 10
y = int(x) + 5
print(y)

b = 10

a = str(b) + " apples"

print('String ' + a)


c = 0

print(bool(c))


# Mathematical function
num = 10

print(abs(-num))
print(pow(2, 3))
print(round(3.7))
print(max(2, 6, 1))
print(min(3, 512, 1))


# String Function

text = "Abdur Shobur is here!"

print(text.upper())  # ABDUR SHOBUR IS HERE!
print(text.lower())  # abdur shobur is here!
print(text.replace("is", "was"))  # Abdur Shobur was here!
print(text.split())  # ['Abdur', 'Shobur', 'is', 'here!']
print(text.split('Shobur'))  # ['Abdur ', ' is here!']


# Basic Function

def greet(name):
    return "Thanks " + name


print(greet("Me!"))


def add(a, b):
    return a+b


print(add(2, 3))
