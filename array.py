# the library of array can be imported as import array
# if you want to add whole array module use this
# array is homogeneous...which mean an array can contain up to same element's data type...it can either be integer
# float or anything else
# for integer use int and for floating point number use float keyword


# from array import *
# my_array = array("I", [1, 2, 3])  # i means signed...and capital I means only unsigned integer
# print(my_array)
# print(my_array.buffer_info())   # this will print the address of the array and the size of the array
# my_array.append(2)
# my_array.remove(1)   # here the argument in remove function means the index...but it starts from 1
# my_array.pop()

# for i in my_array:
#     print(i)

# using the characters in array use the keyword the u

# my_array = array("u", ["a", "b", "c"])
# print(my_array)

# for copying the values of one array to second array
# from array import *
# my_array = array("i", [1, 2, 3])
# new_array = array(my_array.typecode, [a for a in my_array])
# print(new_array)

# getting the input by user for array

# from array import *
#
# my_array = array("i", [])
#
# n = int(input("Enter the number of elements you want to add in array: "))
#
# for i in range(1, n + 1):
#     x = int(input("Enter the {} value: ".format(i)))
#     my_array.append(x)
#
# print(my_array)

# for finding the index of the number
# val = int(input("Enter which value you want to find in the array: "))
#
# counter = 0
# for i in my_array:
#     if i == val:
#         print("The index of {} number is: ".format(val), counter)
#         break
#
#     elif i != val:
#         print("The value", val, "not found in your array")
#         break
#     counter += 1

# adding two numbers

# a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# b = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for i in range(len(a)):
#     for j in range(len(b)):
#         result[i][j] = a[i][j] + b[i][j]
# print(result)

# subtracting the two matrices

# a = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
# b = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
# for i in range(len(a)):
#     for j in range(len(b)):
#         result[i][j] = a[i][j] - b[i][j]
# print(result)

# # multiplying two matrices
#
# a = [[21, 22, 23], [24, 25, 26], [27, 28, 29]]
# b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
#
# for i in range(len(a)):
#     for j in range(len(b)):
#         result[i][j] = a[i][j] * b[i][j]
#
# print(result)
print(r"\" \'\n\t\b")