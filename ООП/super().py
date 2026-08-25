class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

rex = Dog('рекс', 'лабрадор')
print(rex.name, rex.breed)