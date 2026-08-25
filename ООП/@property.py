#============================= GETTER SETTER
# class Account:
#     def __init__(self, balance):
#         self._balance = balance

#     @property
#     def balance(self):
#         return self._balance
#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             raise ValueError('Баланс не может быть отрицательным')
#         self._balance = value

# acc = Account(100)
# print(acc.balance)

# acc.balance = -200
# print(acc.balance)


#==========================COMPUTED PROPERTY
class Account:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    @property
    def area(self):
        return self.width * self.height

r = Account(3, 4)
print(r.area)



