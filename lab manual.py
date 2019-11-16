# for i in range(1, 11):
#     print(i, ",", i ** 2)

# table = int(input("Enter any number: "))
#
# for i in range(1, 11):
#     print(table, "*", i, "=", table * i)


# fibonacci series

# num_terms = int(input("Enter the no. of terms on fibonacci series: "))
#
# first_term = 1
# second_term = 2
#
# counter = 0
#
# while counter < num_terms:
#     print(first_term, end=", ")
#     nth = first_term + second_term  # here second term is = nth term of iteration before
#
#     first_term = second_term
#     second_term = nth
#
#     counter += 1


# n = int(input("Enter the range: "))
# for i in range(1, n + 1):
#
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

n = int(input("Enter the range: "))
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end='')
    print()

