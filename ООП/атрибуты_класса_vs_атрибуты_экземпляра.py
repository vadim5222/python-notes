class Dog:
    species = 'Canis familiars' # атрибут класса (общий для всех)

    def __init__(self, name):
        self.name = name # атрибут экземпляра (у каждого свой)

rex = Dog('Рекс')
buddy = Dog('Бадди')
print(rex.species)
print(buddy.species)
print(Dog.species) 


#========================================Грабли: мутабельные атрибуты класса
class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name

    def learn_trick(self, trick):
        self.tricks.append(trick)

rex = Dog('рекс')
buddy = Dog('бадди')
rex.learn_trick('сидеть')
print(buddy.tricks)

#==========ПРАВИЛЬНО ТАК
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def learn_tricks(self, trick):
        self.tricks.append(trick)

rex = Dog('рекс')
buddy = Dog('бадди')
buddy.learn_tricks('сидеть')
print(buddy.tricks)