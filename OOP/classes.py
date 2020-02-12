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

class Person:
    def __init__(self, name):
        self.name = name

    def greetings(self):
        return "Hi, Have a nice day {}".format(self.name)


# creating an instance

person1 = Person("Aaqib")
print(person1.greetings())