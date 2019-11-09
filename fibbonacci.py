# defining a function for the fibonacci series
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ......


n = int(input("Enter the range of fibonacci series: "))


def fibonacci(n):
    a = 0
    b = 1

    if n < 0:
        print("Enter a positive number please")

    elif n == 1:
        print(a)

    else:
        print(a, end=", ")
        print(b, end=", ")

        for i in range(2, n):
            c = a + b
            a = b
            b = c
            # if c > 100:
            #     break
            print(c, end=", ")


fibonacci(n)
