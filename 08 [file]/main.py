import os
# with open('example.txt', 'r') as file:

#     print(file.read())
# file.close()

# read

with open("example.txt", "a") as file:
    file.write("Hello, me!\n")
    file.write("python is fun\n")


if os.path.exists('example.txt'):
    print('has')
    # os.remove('example.txt')
    # print("delete file")
else:
    print("not")
