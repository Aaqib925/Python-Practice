# program to find out check whether a number is a armstrong number or not

number = input("Enter any number: ")


def func(num):
    """" this function find out the length of the input number and add the total """
    total = 0
    length = len(num)

    for i in range(length):
        total = total + int(num[i]) ** length

    return total


def fun2(total):
    if total == number:
        print("The number {} is Arm Strong number.".format(number))

    else:
        print("The number {} is not a Arm Strong number.".format(number))


(fun2(func(number)))