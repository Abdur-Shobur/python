#  List

fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[-2])  # banana

# list operation
fruits.append("orange")
fruits.insert(0, "grapes")  # in first
popped = fruits.pop()
fruits.remove("banana")
print(fruits, popped)


# list slice
numbers = [1, 2, 3, 3, 4, 3, 5, 6, 6]
print(numbers[:3])
print(numbers[2:])
print(numbers[-2:])
print(numbers[::2])

# Tuples
colors = ("red", "green", "blue")
print(colors[0])
print(list(colors))

colorList = list(colors)
colorList.append("New")
colors = tuple(colorList)
print(colors)

# loop through list tuples
for i in colors:
    print(i)


# nested loop
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print(matrix[0][1])
