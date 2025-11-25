# if
age = 18
if age >= 18:
    print("adult ")


# if else
age = 14
if age >= 18:
    print("Adult")
else:
    print("Minor")


# elif (else if )

mark = 75

if mark >= 80:
    print("A+")

elif mark >= 70:
    print("A")

elif mark >= 60:
    print("A-")

else:
    print("Fail")

#  Comparison operator
Eq = 5 == 5

notEq = 5 != 3

greater = 5 > 3

less = 3 < 4

GreaterOrEq = 5 >= 3

LessOrEq = 3 <= 2


# Logical Operator
age = 20
has_id = True

bothTrue = age and has_id
ifOneTrue = age or has_id
notTrue = not (age and has_id)


# Nested if

if mark == 58:
    if mark >= 80:
        print("Good")
    else:
        print("Pass")

else:
    print("Fail")


# Ternary Operator
status = "Adult" if age >= 18 else "Minor"
print(status)
