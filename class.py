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


class Students():
    number_of_students = 0

    def __init__(self, first, last, roll_number, status):
        self.first_name = first
        self.last_name = last
        self.roll_number = roll_number
        self.status = status
        Students.number_of_students += 1

    # creating a class method similar as functions

    def full_name(self):
        return "The full name of student" + "({})".format(
            self.roll_number) + " is " + self.first_name + " " + self.last_name


student_1 = Students("Aaqib", "Nazir", "CT-47", "present")
print(student_1.__dict__)
student_2 = Students("Abbas", "none", "CT-46", "present")
print(student_1.full_name())


print(student_2.__dict__)
print(student_2.full_name())

print(Students.number_of_students)

