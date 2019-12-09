# # program to find out check whether a number is a armstrong number or not
#
# number = input("Enter any number: ")
#
#
# def func(num):
#     """" this function find out the length of the input number and add the total """
#     total = 0
#     length = len(number)
#
#     for i in range(length):
#         total = total + int(num[i]) ** length
#
#     if int(number) == total:
#         print("The number {} is a Arm Strong number.".format(num))
#     else:
#         print("The number {} is not a Arm Strong number.".format(num))
#
#
# func(number)

def is_armstrong(num):
    num1 = num
    total = 0

    while num1 > 0:
        num2 = num1 % 10

        total += num2 ** len(str(num))

        num1 //= 10
    return total


user_num = int(input("Enter any number: "))

if user_num == is_armstrong(user_num):
    print("The number {} is a Armstrong number.".format(user_num))
else:
    print("The number {} is not a Armstrong number".format(user_num))