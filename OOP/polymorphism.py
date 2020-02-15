# polymorphism is the ability in OOP to use common interface for different data types

class Parrot:
    def fly(self):
        print("Parrots can fly")

    def swim(self):
        print("Parrots can't swim")


class Penguin:
    def fly(self):
        print("Penguins can't fly")

    def swim(self):
        print("Penguins can swim")


# creating instances
parrot = Parrot()
penguin = Penguin()


def flying_test(bird):
    bird.fly()


def swim_test(bird):
    bird.swim()


# passing the instances into the flying test functions

flying_test(parrot)
flying_test(penguin)

swim_test(parrot)
swim_test(penguin)
