# Inheritance is the technique to get all the attributes of the parent class into the child class
# This is done by passing the parameters in the child class of the parent class

class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavour = flavor


class Apple(Fruit):  # inherited from the parent class of Fruits
    pass

class Bannana(Fruit):  # inherited from the parent class of Fruits
    pass