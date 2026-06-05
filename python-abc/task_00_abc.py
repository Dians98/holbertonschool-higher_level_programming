from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by all subclasses."""
        pass


class Dog(Animal):

    def sound(self):
        return "Bark"


class Cat(Animal):

    def sound(self):
        return "Meow"
