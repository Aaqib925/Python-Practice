# class is created by using keyword class and with the name of the class
# self is the prefix...which is called as object
# __init__ is called as instance
# the functions within the class are called are methods


# class human:
#     def __init__(self, name):
#         self.name = name
#         self.age = 10
#
#
# person_one = human("Aaqib")  # this is passing the value to the class
# print(person_one)   # this will print the memory code in which this code is saved
# print(person_one.name)  # this will print the value

# there are 4 major concepts in OOP
# inheritance, encapsulation, polymorphism, abstraction

# inheritance is creating a new class within the class.... which is called derived class or child class to parent class

# the method to restrict the variables or methods within the class is called as encapsulation
# this is done by using underscore or double underscore

# Abstraction means hiding the implementation and showing the user what we want to show only
# in abstract class no instance can be created but child class can be created

# polymorphism is the ability to use the method on various objects
# example class is coloring a shape..but it can be executed for every shape

# in __init__ the first wale underscore are called initial underscore and last wale are called trailing underscore


# class registration:
#     def __init__(self, name, age, roll_no):
#         self.name = name
#         self.age = age
#         self.roll_no = roll_no
#         self.uni_name = "NED university"

# now i will create a method to update uni name

# def update_uni(self, new_uni):
#     self.uni_name = new_uni


# student_1 = registration("Aaqib", 18, "CT-047")
# print(student_1.name, student_1.age, student_1.roll_no, student_1.uni_name)

# student_1.update_uni("KU")   # this will update the value for uni_name
# print(student_1.uni_name)

# print(student_1.__dict__)  # this will print whole data in form of dictionary

# class parent:
#     def __init__(self, first_name, marks):
#         self.first_name = first_name
#         self.marks = marks
#
#     def result(self):
#         print("The Person named {} has {} marks.".format(self.first_name, self.marks))


# creating a object for the parent class
# obj1 = parent("Aaqib", "999")
# obj1.result()


# now a creating a child class of parent class by passing the parent class as an argument

# class child(parent):
#     def result(self):
#         print("That's how mafia works")
#
#
# obj2 = child("Aaqib", 999)
# obj2.result()

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def greetings(self):
#         return "Hi, Have a nice day {}".format(self.name)


# creating an instance

# person1 = Person("Aaqib")
# print(person1.greetings())

# class Fruit:
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor
#
#     def __str__(self):   # __str__ is special method to print the user friendly string
#         return "This apple has {} color and {} flavor".format(self.color, self.flavor)


# jonagold = Fruit("Red", "Sweet")
# print(jonagold)

class Employee:
    # class variable
    raise_amount = 1.04
    # For the total number of employees
    num_employee = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_employee += 1

    # creating a method for full name of any instance

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def description(self):
        return "The Employee {} {} having Email {} has pay {}.".format(self.first, self.last, self.email, str(self.pay))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def increase_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def fromstring(cls, string):
        first, last, pay = string.split("-")
        return cls(first, last, int(pay))

    @staticmethod
    def isworkday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True


# creating instance of Employee class
empl_1 = Employee("Aaqib", "Nazir", 100)
empl_2 = Employee("Test", "User", 100)

# print(empl_1.first)
# print(empl_2.first)
#
# print(empl_1.fullname())
# print(Employee.fullname(empl_2))
#
# print(empl_1.description())
# print(Employee.description(empl_2))

# empl_1.apply_raise()  # for increasing the pay for any instance
# print(empl_1.pay)

# If I wanted to increase the pay for particular instance

# empl_1.raise_amount = 1.05
#
# empl_1.apply_raise()
# print(empl_1.pay)

# If I wanted to change the value of class variable, I can do this by calling the class and then class variable

# Employee.raise_amount = 1.05
#
# print(empl_1.raise_amount)
# print(empl_2.raise_amount)

# print(Employee.num_employee)  # because we created 2 instances out of the class

# Employee.increase_raise_amount(1.06)
# print(Employee.raise_amount)
# print(empl_1.raise_amount)
# print(empl_2.raise_amount)

# using class method as an alternative constructors
# suppose we are passing the string will hyphen separated and we wanted to create a instance using it
# So we need to make a class method, and we will pass that string to that class method

# empl_1_str = "John-DOE-100"
# empl_2_str = "Test-User-100"
# new_empl = Employee.fromstring(empl_1_str)
# new_empl2 = Employee.fromstring(empl_2_str)
#
# new_empl.apply_raise()
# print(new_empl.pay)
#
# print(new_empl2.__dict__)

# Using static method
# import datetime
# mydate = datetime.date(2020, 2, 15)
# print(Employee.isworkday(mydate))
