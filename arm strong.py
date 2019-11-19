# program to find out check whether a number is a armstrong number or not

number = input("Enter any number: ")


def func(num):
    """" this function find out the length of the input number and add the total """
    total = 0
    length = len(number)

    for i in range(length):
        total = total + int(num[i]) ** length

    if int(number) == total:
        print("The number {} is a Arm Strong number.".format(num))
    else:
        print("The number {} is not a Arm Strong number.".format(num))

func(number)

