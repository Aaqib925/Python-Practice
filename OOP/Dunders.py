# creating a class
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.fullname = first + " " + last
        self.pay = pay

