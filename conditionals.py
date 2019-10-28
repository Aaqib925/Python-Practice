# true and false are the boolean functions in python...are if elif and the else are the conditionals
# there are also boolean operators which we will discuss after in the examples

# if and else statements

# language = "Java"
#
# if language == "python":
#     print("The language you are using is python")
# else:
#     print("The language you are using is rather than python")

# language = "python"
#
# if language == "python":
#     print("The language you are using is python")
#
# elif language == "Java":
#     print("The language you are using is Java")
#
# else:
#     print("The language you are using is rather than python and java")


# x = input("Enter the name of the language: ")
# if x == "python":
#     print("The language you are using is 'Python'")
# elif x == "java":
#     print("The language you are using is 'Java'")
# elif x == "rust":
#     print("The language you are using is 'Rust'")
# else:
#     print("The name of language you have written not found.")

# conditions using true and false
# for false we can use...false, Zero(0), None , empty list, tuples and dictionary or sets

# condition = False
# if condition:
#
#     print("You can go to class")
# else:
#     print("You can't go to class, Please wait!")

# there are three of the boolean operators
# for the "and" both conditions should be true

# user = "Admin"
# logged_in = True
#
# if user == "Admin" and logged_in:    # and operator k liye dono cheezon ka hona chaye phr hi wo if condition ko pora karega
#     print("Admin page")
#
# else:
#     print("Something went WRONG!!!")


# user = "Sami"
# logged_in = True
#
# if user == "Admin" or logged_in:    # or operator mn agar koi ek cheez hi true hui to access mil jata ha
#     print("Admin page")
#
# else:
#     print("Something went WRONG!!!")

# not operator(THORA AJEEB SA)


# user = "Admin"
# logged_in = False
# if not logged_in:
#     print("please log in first")
# else:
#     print("Done")

# is and equal examples

# a = [1, 2, 3]
# b = [1, 2, 3]
#
# print(a == b)

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(id(a))
# print(id(b))
# print(id(a) == id(b))

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(id(a))
# print(id(b))
# print(a is b)

# a = [1, 2, 3]
# b = a
# print(id(a))
# print(id(b))
# print(a is b)
