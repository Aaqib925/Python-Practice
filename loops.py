# loops are used ver much..we used for loop in put lists to print out the items

# num = [1, 2, 3, 4, 5]
# for numbers in num:
#     print(numbers)

# num = [22, 23, 34, 45, 55]
# for index, numbers in enumerate(num):
#     print(index,  " - " + str(numbers))

# break and continue two terms are used in the for loop for different function
# break will just stop the loop when the for loop got the condition equals true

# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num)
#     if num == 4:
#         print("Found")
#         break


# number2 = [1, 2, 3, 4, 5]
# for num in number2:
#     if num == 3:
#         print("Found")
#         continue    # continue ka word for loop ki us iteration pa aky found print karwadega...or phr sa continue hojaega loop
#     print(num)

# loop in loop...which is also called nested loops

# num = [1, 2, 3, 4, 5]
# for numbers in num:
#     for letters in "abc":
#         print(letters, numbers)

# loops containing ranges

# for numbers in range(10):
#     print(numbers)

# more defined range syntax

# for numbers in range(1, 12):
#     print(numbers)

# while loops

# x = 1
# while x < 11:
#
#     x += 1
#     print(x)

# x = 0
# while True:
#     if x == 100:
#         print("DONE")
#         break
#     x += 1
#     print(x)


# x = 0
# while True:
#     if x == 100:
#         print("DONE")
#         break
#     x += 1
#     print(x)

# x = 0
# while True:
#     x += 1
#     print(x)

# write a program to print the multiplication table of any input value using while loop
# 
# num = int(input("Enter any number: "))
# i = 1
# while i <= 10:
# 
#     print(num, "*", i, "=", num * i)
#     i += 1


# another method added
# num = int(input("Enter any number: "))
#
# i = 1
# while i <= 10:
#     print(str(num) + "\t*\t" + str(i) + "\t=\t" + str(num * i))
#     i += 1
