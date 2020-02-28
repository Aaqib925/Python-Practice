# creating a class
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.fullname = first + " " + last
        self.pay = pay

    def __str__(self):
        return "The Name of Employee is {} with pay {}".format(self.fullname, str(self.pay))

    def __repr__(self):
        return "Employee ('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # by using the dunders we can specify which function will do what for the class objects
    def __add__(self, other):
        return self.pay + other.pay


empl1 = Employee("Aaqib", "Nazir", 100000)
empl2 = Employee("test", "user", 100000)
print(empl1.__repr__())
print(empl1.__str__())
print(empl1 + empl2)
