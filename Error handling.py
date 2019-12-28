# there are 4 keywords use for the error handling in the code
# try, except, else and finally
# if the code in the try block fails then it goes to the expect block....and then to finally...
# if the code in try block works then the except block will not be executed
# the code in the block of finally is always executed no matter what happens

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    z = a / b
    print("Your answer is: ", z)

except:
    print("Something went wrong...please try again")