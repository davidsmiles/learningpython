from abc import ABCMeta, abstractmethod, ABC


class Animals(metaclass=ABCMeta):

    def walk(self):
        print('walking...')

    @abstractmethod
    def num_legs(self):
        pass


class Dog(Animals):
    def num_legs(self):
        return 4

    def __init__(self, name):
        self.name = name


class Monkey(Animals):
    def num_legs(self):
        return 2

    def __init__(self, name):
        self.name = name


animals = [Dog('dog'), Monkey('monkey')]

for animal in animals:
    print(animal.num_legs())