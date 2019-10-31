# row = 1
# while row < 6:
#     col = 1
#     while col <= row:
#         print("*", end=" ")
#         col += 1
#
#     print("")
#     row += 1

#
# row = int(input("Enter the number of first row: "))
#
# n = int(input("Enter the number of total rows in the pattern: "))
#
# while row < n:     # if we put 10 as value of n then, the last pattern contains 9 stars
#     col = 1
#     while col <= row:
#         print("*", end=" ")
#         col += 1
#     print("")
#     row += 1


# row = int(input("Enter the number of first row: "))
#
# n = int(input("Enter the number of total rows in the pattern: "))
#
# while row < n + 1:   # this will give the same number of stars in tha last line
#     col = 1
#     while col <= row:
#         print("*", end=" ")
#         col += 1
#     print("")
#     row += 1

# row = 1
#
# while row < 6:
#     col = 5
#     while col >= row:
#         print("*", end=" ")
#         col -= 1
#
#     print("")
#     row += 1


# row = 1
# n = int(input("Enter the no. of total rows in the pattern: "))
# column = int(input("Enter the no. of columns of first pattern: "))
# while row < n + 1:
#     col = column
#     while col >= row:
#         print("*", end=" ")
#         col -= 1
#
#     print("")
#     row += 1


# making a pyramid using for loop(right triangle)
# for rows in range(10):
#     print("*" * rows)

# number = int(input("Enter the total number of rows of pattern: "))
#
# for i in range(1, number + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#
#     print("")

# for i in range(6, 1, -1):
#     for j in range(1, i):
#         print("*", end=" ")
#     print()

num = int(input("Enter the number of total rows in pattern: "))

for i in range(num+1, 1, -1):
    for j in range(1, i):
        print("*", end=" ")

    print()
