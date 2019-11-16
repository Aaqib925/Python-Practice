# for i in range(1, 11):
#     print(i, ",", i ** 2)

# table = int(input("Enter any number: "))
#
# for i in range(1, 11):
#     print(table, "*", i, "=", table * i)


# fibonacci series

# num_terms = int(input("Enter the no. of terms on fibonacci series: "))
#
# first_term = 1
# second_term = 2
#
# counter = 0
#
# while counter < num_terms:
#     print(first_term, end=", ")
#     nth = first_term + second_term  # here second term is = nth term of iteration before
#
#     first_term = second_term
#     second_term = nth
#
#     counter += 1


# n = int(input("Enter the range: "))
# for i in range(1, n + 1):
#
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# n = int(input("Enter the range: "))
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end='')
#     print()
#

# n = int(input("Enter the range: "))
# for i in range(n + 1, 0, -1):
#     for j in range(1, i):
#         print(j, end="")
#     print()


# age = int(input("Enter the age: "))
#
# if age < 2:
#     print("The person is baby.")
#
# elif age == 2 or age < 4:
#     print("Toddler.")
#
# elif age == 4 or age < 13:
#     print("Kid.")
#
# elif age == 13 or age < 20:
#     print("Teenager.")
#
# elif age == 20 or age < 65:
#     print("Adult.")
#
# elif age >= 65:
#     print("Older.")

# for i in range(1, 21):
#     if i == 9:
#         continue
#     elif i == 13:
#         continue
#     else:
#         print(i, end=", ")

# year = int(input("Enter the year: "))
#
# if year % 4 == 0:
#     if year % 100 != 0 or year % 400 == 0:
#         print(year, "is a leap year")
#
# else:
#     print(year, "is not a leap year")