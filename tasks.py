# program to count the number of vowels in the String
#
# sentence = input("Enter the String: ")
# vowels = 0
# for i in sentence:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
#         vowels += 1
#
# print("There are", vowels, "vowels in your String")

# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# Consider use range(#begin, #end) method
#
# list1 = []
# for i in range(2000, 3201):
#     if (i % 7 == 0) and (i % 5 != 0):
#         list1.append(i)
#
# print(list1)
#
#
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
# =========CODE============
#
# def fact(x):
#     """ this function calculates the factorial of the input number"""
#     if x == 0:
#         return 1
#     else:
#         return x * fact(x - 1)
#
#
# x = int(input("Enter any number: "))
# if x != 0:
#     print("The factorial of", x, "is", fact(x))
# else:
#     print("The factorial of 0 is 1")
#
# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# =======CODE==========
# n = int(input("Enter any number: "))
# dictionary = {}
#
# for i in range(1, n + 1):
#     dictionary[i] = i * i
#
# print(dictionary)
#
#
# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
#
# ===========CODE================
#
# values = input("Enter the values: ")
# result = values.split(",")
# t = tuple(result)
# print(result)
# print(t)
#
#


# Question:
# write a program which takes imput of the marks of the subjects and prompt the grade to the user

# sub1 = int(input("Enter marks in Chemistry: "))
#
# sub2 = int(input("Enter marks in Physics: "))
#
# sub3 = int(input("Enter marks in Maths: "))
#
# sub4 = int(input("Enter marks in Comp Sci: "))
#
# sub5 = int(input("Enter marks in Urdu: "))
#
#
# per = ((sub1 + sub2 + sub3 + sub4 + sub5) / 500) * 100
#
# print("Your percentage is: ", per)
#
# print("Your grade is: ", end="")
#
# if per <= 100 and per >= 80:
#     print("A1")
#
# elif per < 80 and per >= 70:
#     print("A")
#
# elif per < 70 and per >= 60:
#     print("B")
#
# elif per < 60 and per >= 50:
#     print("C")
#
# elif per < 50:
#     print("Fail")

# Let's learn about list comprehensions! You are given three integers X, Y and Z representing the dimensions of a cuboid along with an
# integer N. You have to print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k  is not
# equal to N. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z
#
# Input Format
# Four integers X, Y, Z and N each on four separate lines, respectively.
#
# Constraints
# Print the list in lexicographic increasing order.
#
# Sample Input
# 1
# 1
# 1
# 2
#
# Sample Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
#
#
# Enter your code here. Read input from STDIN. Print output to STDOUT

# x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#
# result = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != n]
# print(result)


# n = int(input())
#     arr = map(int, input().split())
#
#     print(sorted(list(set(arr)))[-2])

# the guessing game

# import random
#
# comp_choice = random.randint(1, 20)
# print(comp_choice)
#
# my_guess = int(input("Guess the number chosen by the computer: "))
#
# if my_guess > comp_choice:
#     print("Your guess was too high")
#
# elif my_guess < comp_choice:
#     print("Your number is too low")
#
# elif my_guess == comp_choice:
#     print("You guessed the correct number!!")

# program to calculate the square root of positive and complex numbers

# import math
#
# num = int(input("Enter any positive number: "))
# if num < 0:
#     print("Please enter a positive number")
#
# print("The sqaure root of", num, "is: "math.sqrt(num))

# import cmath
#
# num = complex(input("Enter any complex number: "))
#
# print("The square root of complex number", num, "is: ", cmath.sqrt(num))

# program to calculate the area of a triangle
#
# import math
#
# a = float(input("Enter the first side of triangle: "))
# b = float(input("Enter the second side of triangle: "))
# c = float(input("Enter the third side of triangle: "))
#
#
# def para():
#     """ calculates the value of parameter of the triangle """
#     parameter = (a + b + c) / 2
#     return parameter
#
#
# def area(parameter):
#     """ Calculates the area of a triangle """
#     answer = math.sqrt(parameter * (parameter - a) * (parameter - b) * (parameter - c))
#     return "The area of the triangle is %0.2f " % answer
#
#
# print(area(para()))

# program to solve the find out the root if quadratic equation

# import math
#
# print("Solve the quadratic equation ax^2 + bx + c = 0")
# a = int(input("Enter the value of coefficient of x^2: "))
# b = int(input("Enter the value of coefficient of x: "))
# c = int(input("Enter the constant value: "))
#
#
# def discrim():
#     """ Calculates the discriminant of the equation """
#     discriminant = math.sqrt((b**2) - (4 * a * c))
#     return discriminant
#
#
# def roots(discriminant):
#     """ Calculates the roots of the equation """
#     x1 = (-b + discriminant) / 2 * a
#     x2 = (-b - discriminant) / 2 * a
#     return "The roots of equation {}x^2 + {}x + {} are: ".format(a, b, c), x1,  x2
#
#
# print(roots(discrim()))

# swapping the value of 2 variables

# x = 22
# y = 33
#
# x, y = y, x
#
# print("The value of x after swapping is: ", x)
# print("The value of y after swapping is: ", y)


# write a program to calculate the armstrong number

# num = int(input("Enter any number: "))
#
# # this is value in which the total of cubes of number will be added
# sum = 0
#
# num2 = num # initializing another variable so we could the num value with sum...
#
# while num2 > 0:
#     num3 = num2 % 10  # this operation gives us each number for making cube separately
#
#     sum += num3 ** 3  # adding the cube of single number from num to sum variable
#     # print(sum)
#     num2 //= 10   # this is going to remove the last number from the num value
#
# if num == sum:
#     print("The number {} is an Armstrong number".format(num))
#
# else:
#     print("The number {} is not Armstrong number".format(num))


# write a program to generate the square of the numbers


# n = int(input("Enter the range of the numbers: "))
# for i in range(1, n + 1):
#     print("The square of", i, "is",  i ** 2)

# now making a function which calculate the square of the numbers

# def sq(n):
#
#     for i in range(1, n + 1):
#         print("The square of", i, "is", i ** 2)
#
# sq(10)
#
# lst = [[x for x in range(3)] for y in range(3)]
#
# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 == 0:
#             print("#")


# tup = (1, 2, 4, 8)
# tup = tup[-2: -1]
# print(tup)
# tup = tup[-1]
# print(tup)

# lst = [1, 2]
#
# for v in range(2):
#     lst.insert(-1, lst[v])
#
# print(lst)

# d = {"1": "0", "0": "1"}
#
# for x in d.values():
#     print(x, end="")