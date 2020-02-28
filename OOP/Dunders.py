# creating a class
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.fullname = first + " " + last
        self.pay = pay

    def __str__(self):
        return "The Name of Employee is {} with pay {}".format(self.fullname, self.pay)

