# For Loop


fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# For Loop with range

# range(start, stop, step )

# 0 to 4
for i in range(5):
    print(i)


# 1 to 5
for i in range(1, 6):
    print(i)

# 2 to 10 step 3
for i in range(2, 11, 3):
    print(i)


# while loop

i = 1
while i <= 5:
    print("while " + str(i))
    i += 1


# break and continue
for i in range(1, 10):
    if i == 5:
        break
    print("break ", str(i))

# continue
for i in range(1, 10):
    if i == 3:
        continue  # skip 3
    print(i)


# nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j{j}")


# loop with else

for i in range(1, 4):
    print(i)
else:
    print("Finished")


# The while loop prints the multiplication table for the number n.
n = int(input("Number: "))

i = 1
while i <= 10:
    print(f"{n}x{i} = {n * i}")
    i += 1


rows = n
for r in range(1, rows+1):
    for c in range(r):
        print("*", end="")

    print()
