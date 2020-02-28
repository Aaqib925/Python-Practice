# creating a class

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)


empl1 = Employee("Aaqib", "Nazir")
print(empl1.fullname)
print(empl1.email)