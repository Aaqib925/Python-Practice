# creating a class

# class Employee:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     @property
#     def fullname(self):
#         return "{} {}".format(self.first, self.last)
#
#     @property
#     def email(self):
#         return "{}.{}@company.com".format(self.first, self.last)
#
#
# empl1 = Employee("Aaqib", "Nazir")
# empl1.first = "Hello"
# print(empl1.fullname)
# print(empl1.email)

# getter setters and deleters

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)


emp1 = Employee("Aaqib", "Nazir")
print(emp1.fullname)
emp1.fullname = "Test User"
print(emp1.first)
print(emp1.last)
print(emp1.fullname)
print(emp1.email)