# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f'{self.name} ест')

# class Dog(Animal): # Dog - наследуется от Animal
#     def bark(self):
#         print(f'{self.name}: гав')

# rex = Dog('рекс')
# print(rex.name)
# rex.eat() # рекс есть - унаследовано от Animal
# rex.bark() # рекс гав - свое


# ======================Переопределение
class Animal:
    def speak(self):
        print('Какой-то звук')

class Dog(Animal):
    def speak(self): #override 
        print('Гав')

class Cat(Animal):
    def speak(self):
        print('Мяу')


for a in [Dog(), Cat(), Animal()]:
    a.speak()