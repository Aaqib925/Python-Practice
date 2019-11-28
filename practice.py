# message = "Hello World"
# print(len(message))
# print(message[3])
# print(message[0:6])     this is used for the range...but the last index is exlusive this is called slicing

# print(message.lower())   this changes the text to lower case
# print(message.upper())   this changes the text to upper case
# print(message.count("l"))    this counts the number of anything used in the string
# print(message.find("World"))  this gives the index of the world we are writing in the brackets

# replace function
# message = message.replace("World", "Universe")
# print(message)

# adding two or more strings

# greetings = "Hello"
#
# name = "world"

# message = greetings + ", " + name
# print(message)

# print(str(greetings) + ", " + str(name))

# using format method of strings

# message = "{}, {}".format(greetings, name)
# print(message)

# using the f strings method in python3.6 or above

# message = f"{greetings}, {name}"
# print(message)

# f strings are usefull for example

# message = f"{greetings.upper()}, {name.upper()}"
# print(message)

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()
#
# for i in range(6, 0, -1):
#     for j in range(1, i + 1):
#         print("*", end="")
#
#     print()

row = 0
while row <= 5:
    col = 0
    while col <= row:
        print("*", end="")
        col += 1
    print()
    row += 1
