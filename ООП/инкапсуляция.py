class Account:
    def __init__(self, balance):
        self.balance = balance #public - можно трогать снаружи
        self._internal = "secret" #protected - не трогай без нужды
        self.__pin = '1234' #private - name mangling


acc = Account(100)
print(acc.balance)
print(acc._internal)
print(acc._Account__pin)