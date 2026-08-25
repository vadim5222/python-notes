from typing import Protocol

class Quackable(Protocol):
    def quack(self) -> None: ...

class Duck:
    def quack(self) -> None:
        print('КРЯ')

class Person:
    def quack(self) -> None:
        print('Я тоже так могу')

def make_it_quack(x: Quackable) -> None:
    x.quack()

make_it_quack(Duck()) #ок у Duck есть quack()
make_it_quack(Person()) #ок у Person тоже есть quack()