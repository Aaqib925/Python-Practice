"""
This is the simple guessing game which takes three input from the user and 2 are automatically input by the computer
The main logic is that when the user input's the first number, it prompt the user the total addition of numbers, which
would be the guess after the addition of all five numbers
"""

print("Welcome to the game!! ", end="")
print("The result will be equal to the number which i will show you in second step")

# first input (by user)

x = int(input("Enter first two digit number: "))

# prompting the user the the total addition of the numbers in second step

print("Your total according to my guess is: ", x + 198)

#  second input (by user)

y = int(input("Enter the second two digit number: "))


# using for loop to make the output look lenghty

for i in range(3):
    print("Calculating!!")
# third number will be added by the computer which will be equal to 99 - second number

z = 99 - y

# prompting the user, which third number is added by computer

print("Third number added by me is: ", z)

# 4th input(by user)

a = int(input("Enter the fourth two digit number: "))

# using for loop to make output look lengthy

for i in range(3):
    print("Calculating!!")


# fifth number will be added by the computer which will be equal to 99 - fourth number

b = 99 - a

# prompting the user which number is added by me

print("Fifth number added by me is: ", b)

# total addition of all numbers

result = x + y + z + a + b

# prompting the user addition of all numbers in the form of string

print(x, "+", y, "+", z, "+", a, "+", b, "=", result)
