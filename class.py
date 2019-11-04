# class Employee():

# making an init to make the instance for future use
# def __init__(self, first, last, pay):  # we are using the self as the basic argument of the init method
#     self.first = first
#     self.last = last
#     self.pay = pay

# defining a method(similar to the function) in a class

# def full_name(self):  # creating a method...argument self is necesaary
#     return "{} {}".format(self.first, self.last)


#  making an instance for the class
# employee_1 = Employee("Aaqib", "Nazir", "100k")
# employee_2 = Employee("Test", "User", "100k")


# printing the attributes of the class

# print(employee_1.first)
# print(employee_1.last)
# print(employee_1.pay)
# # implementing the method in the instances
# print(employee_1.full_name())
#
# print(employee_2.first)
# print(employee_2.last)
# print(employee_2.pay)
#
# print(employee_2.full_name())

# print(employee_1.__dict__)
# print(employee_2.__dict__)


# class variables....wo variables jo k class k har instance k liye available hote hen for different modifications
# class Employee():
#     raise_amount = 1.04  # now i have to add this variable to the method where it is required
#     number_of_employees = 0
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.mail = first + last + "@company.com"
#         Employee.number_of_employees += 1
#     def full_name(self):
#         return self.first + self.last
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#
# emp_1 = Employee("Aaqib", "Nazir", 10000)
# emp_2 = Employee("Test", "User", 90000)

# print(emp_1.full_name())
# print(emp_2.full_name())
#
# print(emp_1.__dict__)
# print(emp_2.__dict__)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
#
# print(emp_2.pay)
# emp_2.apply_raise()
# print(emp_2.pay)   # this is alot more diffcult...so i am gonna assign a variable class above

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)


# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# emp_1.apply_raise()
# emp_2.apply_raise()
# print(emp_1.__dict__)
# print(emp_2.__dict__)


# if we want to change the raise amount number for specific employee

# emp_1.raise_amount = 1.05
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# to find out the number of employees we create class varible of number of variables
# print(Employee.number_of_employees)


# class Students():
#     number_of_students = 0
#
#     def __init__(self, first, last, roll_number, status):
#         self.first_name = first
#         self.last_name = last
#         self.roll_number = roll_number
#         self.status = status
#         Students.number_of_students += 1
#
#     # creating a class method similar as functions
#
#     def full_name(self):
#         return "The full name of student" + "({})".format(
#             self.roll_number) + " is " + self.first_name + " " + self.last_name
#
#
# student_1 = Students("Aaqib", "Nazir", "CT-47", "present")
# print(student_1.__dict__)
# student_2 = Students("Abbas", "none", "CT-46", "present")
# print(student_1.full_name())
#
#
# print(student_2.__dict__)
# print(student_2.full_name())
#
# print(Students.number_of_students)

# There are 3 methods involved in classes...regulat...static...and class methods

# there is a lot of difference between a regular method, class method and a static method...actually the regular method
# takes self as an first argument...class methods use cls(class) as an first argument which are also called as
# alternative constructors....and the static methods actually do not take self or class as there arguments...they are
# just like an function in the class

# Class method

# creating a class of an employee
import datetime
class Employee:

    # creating a regular class method which takes self as first argument

    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        self.pay = pay

    # now i am going to create a class variable to increase the pay of the Employee...which takes cls(class) as
    # argument

    @classmethod
    def raise_pay_amt(cls, amount):
        cls.raise_amount = amount

    # creating a static method which does not take instance self and class ass first argument
    # in python the date time module has sunday == 6 and saturday == 5 after using a date time module
    # importing date time module in last lines
    @staticmethod
    # creating a static method to check if the a working day or not
    def is_workday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True


employee_1 = Employee("Aaqib", "Nazir", 10000)
employee_2 = Employee("Test", "User", 10000)
employee_3 = Employee("test", "user", 10000)

# now i am using the class method to increase the pay of the every employee without using the instance

# Employee.raise_pay_amt(1.04)
# print(employee_1.raise_amount)
# print(employee_2.raise_amount)
# print(employee_3.raise_amount)

# the class variable changed the pay of every single Employee instance



# creating a my today's date variable using datetime module

my_date = datetime.date(2019, 30, 3)
print(Employee.is_workday(my_date))
