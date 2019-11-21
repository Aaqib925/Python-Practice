# program to count the number of vowels in the String
#
# sentence = input("Enter the String: ") vowels = 0 for i in sentence: if i == "a" or i == "e" or i == "i" or i ==
# "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U": vowels += 1
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
# Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that
# is an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose
# the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25,
# 6: 36, 7: 49, 8: 64}
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
# Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and
# a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,
# 98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
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

# Let's learn about list comprehensions! You are given three integers X, Y and Z representing the dimensions of a
# cuboid along with an integer N. You have to print a list of all possible coordinates given by (i, j, k) on a 3D
# grid where the sum of i + j + k  is not equal to N. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z
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
#
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

# def fun(a, b):
#     return b ** a
#
# print(fun(b = 2, 2))

# list = [x * x for x in range(5)]
# print(list)

# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y - 1)
#
# print(fun(0, 3))

# def fun1(a):
#     return None
#
# def fun2(a):
#     return fun1(a) * fun1(a)
#
# print(fun2(2))
# i = 0
# while i < i + 2:
#     i += 1
#     print("*")
# else:
#     print("*")


# Write a program to convert kilometers into miles
# 1 kilometer = 0.621371 miles

# print("1. Convert kilometer into miles.")
# print("2. Convert miles into kilometers.")
#
# x = int(input("Enter number of which conversion you want: "))
#
# con_factor = 0.621371  # since 1 kilometer is = 0.621371 miles
#
# if x == 1:
#     print("=========Kilometers into miles conversion=========")
#
#     km = float(input("Enter value you want to covert in miles: "))
#
#
#     def ktm():
#         miles = km * con_factor
#         return "%2f" % miles
#
#
#     print(km, "kilometers are equal to:", ktm()+" miles")
#
# elif x == 2:
#     print("=======Miles into kilometer conversion======")
#
#     mil = float(input("Enter the value to convert into kilometers: "))
#
#
#     def mile():
#         kilometers = mil / con_factor
#         return "%2f" % kilometers
#
#
#     print(mil, "miles are equals to:", mile()+" kilometers")
#
# else:
#     print("Invalid choice, Please enter correct choice number.")


# write a program to convert celsius into fahrenheit and vice versa

# print("Please select one choice.")
# print("1. Convert Celsius into Fahrenheit.")
# print("2. Convert Fahrenheit into Celsius.")
#
# choice = int(input("Enter your choice of conversion: "))
#
# if choice == 1:
#     print("===========Celsius to Fahrenheit conversion==========")
#     cel = float(input("Enter the value you want to convert in Fahrenheit: "))
#
#     def fah():
#         fahrenheit = (cel * 1.8) + 32
#         return "%0.2f" % fahrenheit
#     print(cel, "Celsius is equals to: ", fah()+" fahrenheits")
#
# elif choice == 2:
#     print("==========Fahrenheit to Celsius conversion============")
#
#     far = float(input("Enter the value you want to convert in Celsius: "))
#
#     def cel():
#         celsius = (far - 32)/1.8
#         return "%0.2f" % celsius
#     print(far, "Fahrenheits are equal to: ", cel()+" celsius")
#
# else:
#     print("Invalid choice, Please enter correct choice number.")


# program to check whether the year is leap year or not condition 1 = if year is divisible by 4 then...it should be
# divisible by 100 and if its true then it should be divisible by 400 also...if not...then year is not the leap year


# year = int(input("Enter the year: "))
#
#
# def isleap(year):
#     if year % 4 == 0:
#         if year % 100 != 0 or year % 400 == 0:
#             print("{} is a leap year".format(year))
#         else:
#             print("{} is not a leap year".format(year))
#     else:
#         print("{} is not leap year".format(year))
#
#
# isleap(year)


# Program to find whether a number is prime number or not...and if not...then explain how...by showing the factors of it
# prime number is that number which do not have any factors except itself


# num = int(input("Enter any number: "))

# we have to write a code by which we can check whether the factors of number exist or not
#
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number.")
#             print(i, "times", num // i, "is", num)
#             break
#     else:
#         print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")


# program to find out the factors of a given number

# num = int(input("Enter any number: "))
#
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i, "times", num // i, "is", num)


# program to print the prime numbers in a interval

# lower = int(input("Enter the upper limit: "))
# upper = int(input("Enter the lower limit: "))
#
# print("Prime numbers in the interval", lower, "and", upper, "are:")
# count = 0
# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)
#             count += 1
#
# print("There are", count, "prime numbers in interval", lower, "and", upper)

# write a program to print the factorial of the any number

# num = int(input("Enter any number: "))
# factorial = 1
# if num < 0:
#     print("The factorial of negative number does not exist.")
#
# elif num == 0 or num == 1:
#     print("The factorial of", num, "is 1")
#
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print("This factorial of {} is".format(num), factorial)

# program to print the multiplication table

# num = int(input("Enter any number: "))
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# program to print the fibonacci series 0, 1, 2, 3, 5, 8 ....

# first the number of terms you want to get in certain fibonacci series

# n_terms = int(input("Enter the number of terms you want in the fibonacci series: "))
#
# first_num = 0
# sec_num = 1
#
# counter = 0
# if n_terms == 0 or n_terms == 1:
#     print(first_num)
#
# elif n_terms < 0:
#     print("Please enter a positive number.")
#
# else:
#     print("The fibonacci series is: ", end="")
#     while counter < n_terms:
#         print(first_num, end=", ")
#         nth = first_num + sec_num
#
#         first_num = sec_num
#         sec_num = nth
#         counter += 1


# write a function to count number of integer in a number

# num = int(input("Enter any number to find out it's length: "))
#
#
# def num_counter(any_num):
#     """ function to count the number of int in a number """
#     counter = 0
#     while any_num > 0:
#         any_num = any_num // 10
#         counter += 1
#     return counter
#
# write a program to check what number is repeated in the list
#
# num = int(input("Enter the range of your list: "))
#
# my_inp_list = []
#
# for i in range(num):
#     x = int(input("Enter numbers you want to include in your list: "))
#     my_inp_list.append(x)
#
# print("Your list is: ", my_inp_list)
#
# repeated_values = []
#
#
# def check_repeated(my_list):
#     for i in range(len(my_list)):
#         for j in range(i + 1, len(my_list)):
#             if my_list[i] == my_list[j] and my_list[i] not in repeated_values:
#                 repeated_values.append(my_list[i])
#     return repeated_values
#
#
# print(""" Enter your choice:
# 1. if you want to check which number is repeated in the list
# 2. Exit """)
#
# choice = int(input("Enter any choice: "))
#
# if choice == 1:
#     print("The values repeated in the list are: ", check_repeated(my_inp_list))
# else:
#     print("Thank You")

# write a program which converts decimal into binary number

# num = 10
# ls = []
# while num > 1:
#     remainder = num % 2
#
#     ls.append(remainder)
#
#     num //= 2
#     if num == 1:
#         ls.append(1)
#
# ls2 = ls.reverse()
# print(ls2)

num = 50
total = ""
while num > 1:
    remainder = num % 2
    total = str(remainder) + total

    num //= 2
    if num == 1:
        total = str(1) + total

print(total)

print(bin(50))