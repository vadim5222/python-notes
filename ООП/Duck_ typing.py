class Duck:
    def quack(self):
        print('кря')

class Person:
    def quack(self):
        print('Я тоже могу крякнуть')

def make_it_quack(thing):
    thing.quack()


make_it_quack(Duck())
make_it_quack(Person())