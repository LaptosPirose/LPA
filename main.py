import numpy as np
from time import time


class Dog:
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age

    def bark(self):
        return f'{self.__name} is barking!'

    def get_name(self):
        return self.__name


def main():
    rex = Dog('Rex', 10)
    print(rex.get_name())
    print(rex.__class__.__name__)
    print(Dog.__name__)
    print(rex.bark())


if __name__ == '__main__':
    main()
