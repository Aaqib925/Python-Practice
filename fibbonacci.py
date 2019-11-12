# defining a function for the fibonacci series
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ......


# n = int(input("Enter the range of fibonacci series: "))
#
#
# def fibonacci(n):
#     a = 0
#     b = 1
#
#     if n < 0:
#         print("Enter a positive number please")
#
#     elif n == 1:
#         print(a)
#
#     else:
#         print(a, end=", ")
#         print(b, end=", ")
#
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#             # if c > 100:
#             #     break
#             print(c, end=", ")
#
#
# fibonacci(n)


# recursive function example which repeat itself over and over and over
# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return  1
#     elif n > 2:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# for n in range(1, 11):
#     print(n, ":", fibonacci(n))

# Memoization ( to delete the cache values )

# from functools import lru_cache
#
# @lru_cache(maxsize= 1000)
#
# def fibonacci(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     if n > 2:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# for n in range(1, 100):
#     print(n, ":", fibonacci(n))
