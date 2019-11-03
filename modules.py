# import my_module  # i imported that module by import keyword
#
#
# course = ["Maths", "Physics", "Chemistry", "CompSci"]
# # to use the function of the imported module..we have to write down the name of the module first and then the function name
#
# index = my_module.find_index(course, "Physics")
#
# print("The index of the required subject is: ", index)

# as here the my_module is using alot of room so we can specify any name for it...after importing the module
# import my_module as mm...so we can use mm instead of my_module

# we can import everything by using import my_module *

# from my_module import find_index, test   # this is gonna import the index function and test string
#
# course = ["Maths", "Physics", "Chemistry", "CompSci"]
#
# index = find_index(course, "Maths")
# print(index)
# print(test)

# using the built in module of random and using it in our code

# import random
#
# course = ["Maths", "Physics", "Chemistry", "CompSci"]
#
# random_value = random.choice(course)
#
# print(random_value)

# using the math module from standard libray

# import math
#
# rad = math.radians(90)
#
# print(rad)
#
# print(math.sin(rad))
# print(math.cos(rad))
# print(math.tan(rad))

# using the module of datetime and calendar to find the leap year from the std library

# import datetime
# import calendar
# today = datetime.date.today()
# print(today)
#
# leap_year = calendar.isleap(2020)
# print(leap_year)

# using the os module from the std library to get the path of the current working directory

# import os  # this module can be useful to create or delete directories as well
# print(os.getcwd())  # current working directory
#
# print(os.__file__)

# import antigravity

