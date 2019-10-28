# functions in the python are created by using the keyword (def) and there are two ways to define any of the function
# one method is to make the function and then to call it after anywhere in the code
# the advantage of making the function is that if we want any change throughout the code...we can just change our
# function to make changes all over the code
# in the function...there are two methods...print(>>>) or return(>>>>)
# in the print case we have to call the function after in the code with the name of the function with the round braces
# but in the return case...we just use the print keyword and then add the name of the function where used

# print case
#
# def main():
#     print("Hello")
#
# main()

# def main():
#     return "Hello World"
#
# print(main)      # this will only show the place where the function is save
# def main():
#     return "Hello World"
#
# print(main())     # this can return the value of the what we have declared in the function

# if you want something to add in the function

# def main(name, age):
#     print({}, {}).format(name, age)
#
# main(name, age)

# def hello_function():
#     pass       # by this keyword pass we can leave any function blank

# def main():
#     pass
#               #this code is showing where the function is saved in the memory..if we not use brackets while calling function
# print(main())

# def hello_func():
#     print("Hello World")
#
# hello_func()   # in this way we can call any of the function

# def hello_func():
#     return "Hello World"
#
# print(hello_func())   # in this case we have to use the print keyword to get the returned value
#
#
# def hello_func():
#     return "Hello World"
#
# print(hello_func().upper())   # this is very usefull if we want to get the returned value changed like
# print(hello_func().lower())
# print(hello_func().find("l"))

# method to pass the argument in the function

# def main(greeting):    # mene yahan pa argument pass kia greeting name sa...
#     return "{}, World".format(greeting)
#
# print(main("HI"))    # ab mjhe yahan pa us parameter ko fill karna hoga


# def main(greeting, name):
#     return "{}, {}".format(greeting, name)
#
# print(main("HI", "Aaqib"))    # in this case if i will leave the name parameter empty...this will show me an error
#
# def main(greeting, name = "ASIM"):
#     return "{}, {}".format(greeting, name)
#
# print(main("Hello"))   # in this code mene upar argument pass karte hoe hi default value rkhdi thi name ki asim..ilye khali
# error nahi ayaa.

# *args stands for arguments and **kwargs stands for keyword arguments..i means k kwargs mn hamen pehle key deni hogi
#
# def main(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# main("Maths", "Physics", "Chemistry", name = "Aaqib", age = "18") # these are called postionals arguments
#
# in this way we can gather our information in more easy way by using function and then by passing parameters args and kwargs

# args wali information is in the form of tuple...and the kwargs need keys that why it is dictionary

# def main(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# courses = ["Maths", "Physics", "Chemistry"]
#
# student_info = {"name": "Aaqib", "age": "18"}
#
# main(courses, student_info)    # here i passes courses and student_info as the postitional argument
# # but this will not give as reuired output...cuz args and kwargs are not diffrentiatted
#
# def main(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# courses = ["Maths", "Physics", "Chemistry"]
# student_info = {"name": "Aaqib", "age": "18"}
#
# main(*courses, **student_info)  # this is correct method to set something as positional argument...here values are unpacked

# code for the determination if the year is the leap year or not..and to calculate the days of in month w.r.t year

# 0 is just for the place holder...to make index equal...cuz 0 month nahi hote na
# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
#
# def is_leap(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
# def days_in_month(month, year):
#
#     if not 1 <= month <= 12:
#         return "INVALID MONTH"
#
#     if month == 2 and is_leap(year):
#         return 29
#
#     return month_days[month]
#
# print(is_leap(2020))
# print(days_in_month(22, 2020))

# n = 3
# for i in range(1, n + 1):
#     print(i, end="")
