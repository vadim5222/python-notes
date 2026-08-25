# =========================================== Instance метод
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self): # instance метод
#         print(f'{self.name} говорит гав')

# my_dog = Dog("рекс", 3)
# my_dog.bark()


# ==============================================Class methods
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def puppy(cls, name):
#         return cls(name, age=0)

# rex = Dog.puppy('рекс')
# print(rex.name)

# ============================================================Static method
# class Dog:
#     @staticmethod
#     def is_valid_age(age):
#         return 0 <= age <= 30

# my_dog = Dog()
# print(my_dog.is_valid_age(5))
# print(my_dog.is_valid_age(31))