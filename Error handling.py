# there are 4 keywords use for the error handling in the code
# try, except, else and finally
# if the code in the try block fails then it goes to the expect block....and then to finally...
# if the code in try block works then the except block will not be executed
# the code in the block of finally is always executed no matter what happens

# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print(a/b)
#
# except ZeroDivisionError:
#     print("Denominator can never be zero.")
#
# except ValueError:
#     print("Please enter a integer.")
#
# else:
#     print("This is else block...no error found in the try block")
#
# finally:
#     print("This is finally block....I am gonna run what ever it is..huhu")


# we can also raise an exception by using th keyword raise with the exception

# x = int(input("Enter any positive number: "))

# if x < 0:
#     raise Exception("Please enter positive number.")  # but this is going to print the exception like error
# else:
#     print(x)

