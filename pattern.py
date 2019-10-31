# row = 4
# while row < 10:
#     col = 1
#     while col <= row:
#         print("*", end="")
#         col += 1
#
#     print("")
#     row += 1

#
# row = int(input("Enter the number of first row: "))
#
# n = int(input("Enter the range of the pattern: "))
#
# while row < n:     # if we put 10 as value of n then, the last pattern contains 9 stars
#     col = 1
#     while col <= row:
#         print("*", end="")
#         col += 1
#     print("")
#     row += 1


row = int(input("Enter the number of first row: "))

n = int(input("Enter the range of the pattern: "))

while row < n + 1:   # this will give the same number of stars in tha last line
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print("")
    row += 1
