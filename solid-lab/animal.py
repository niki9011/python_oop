from abc import ABC, abstractmethod

class Animal:

    @abstractmethod
    def animal_sound(self):
        pass


class Cat(Animal):

    def animal_sound(self):
       return 'meow'

class Dog(Animal):

    def animal_sound(self):
        return 'woof-woof'


class Chicken(Animal):

    def animal_sound(self):
        return 'cluck'


animals = [Cat(), Dog(), Chicken()]

for animal in animals:
    print(animal.animal_sound())
