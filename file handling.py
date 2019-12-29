# we can create our files in the same directory and access them in our code by using some code
# to open any file mn use open() function and to close we use close() along with the variable of that file
# my open the file my using the open function...but there also methods by which we can change the mode in which we
# wanna open our file...like "r" for read mode, "a" for append mode, "w" for write mode, "t" for text mode
# for reading the lines of the file we use read()...in the parenthesis we can pass the integer value which is the
# range of how many lines we wanna print..to read one whole line we use readline() and for reading all lines we use
# readlines....for writing or adding lines in our particular file we use the mode as append...and for writing into
# file we can use the write function
#
#
# now i will create a file by using open keyword...but by using the mode...else it will show me error of file not found
#
# f = open("text.txt")
# print(f)
#
# f = open("text.txt", "r")  # this will create a file...
# print(f.read())
# print(f.readline(), end="")
# print(f.readline(), end="")
#
# print(f.readlines())  # this will print all the lines...and then shows in the list
#
# for x in f:
#     print(x)
#
# f = open("text.txt", "a")
# f.write("Hello")
#
# f = open("text.txt", "w")    # write will overwrite all the contents where as append will add in the last of the file
# f.write("Aaqib")
# f = open("text.txt", "r")
# print(f.readlines())
#
# if you want to open a image file ...we use mode of rb...which means read binary....but will show us the hexa code
# which are the pixels of that image file
#
# you also delete a file my importing the os and then delete file
#
# import os
# os.remove("text.txt")  # this will delete the file
#
# we can delete the directory by using the syntax os.rmdir() and passing the directory name..but the
# directory must be empty
#
# lab manual exercise
#
# f = open("employee.txt", "a")
#
# emplo_id = input("Enter the id of employee: ")
# emplo_name = input("Enter the name of employee: ")
# emplo_salary = input("Enter salary of employee: ")
#
# f.write(emplo_id)
# f.write("\n")
# f.write(emplo_name)
# f.write("\n")
# f.write(emplo_salary)
# print("\n")
#
# f = open("employee.txt", "r")
# print(f.read(), end="")
#
# f.close()
