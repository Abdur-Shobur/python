# 1. Basic Function
def great():
    print("Hello, Abdur Shobur!")


# 2. Function with Parameters
def great(name):
    print("Hello ", name)
# great("")


# 3. Function with Return Values
def add(a, b):
    return a+b
# print(add(1, 2))


# 4. Default Parameters
def defName(name="Guest"):
    print(f"Hello, {name}")
# defName("Me")
# defName("")
# defName()


# 5. Keyword Arguments
def personalInfo(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")
# personalInfo("Abdur", 12, "Test")


# 6. Variable Scope
# local are in side function
# global are outside function, that access anywhere

x = 10  # Global


def func():
    y = 5  # local
    print(x + y)
# func()


# Modifying Global Variables
x = 10


def modifyGlobal():
    global x
    x = 20
# modifyGlobal()


# 7. Lambda (Anonymous) Functions
def add2(a, b): return a + b
# add = lambda a,b:a+b
