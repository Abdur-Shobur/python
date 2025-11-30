# print(10 / 0) # error

# try except
""" 
try:
    x = int(input("Number: "))
    result = 10 / x
    print(result)

except ZeroDivisionError:
    print("Error: Can not divide 0")

except ValueError:
    print("Inter Valid Number")
"""

# multiple error
""" 
try:
    num = int(input("Number: "))
    print(10 / num)

except (ValueError, ZeroDivisionError) as e:
    print("error", e)
"""

# finally block

age = int(input("Enter Age: "))
if age <= 0:
    raise ValueError("Age can not be negative")
