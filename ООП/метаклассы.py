# class Foo:
#     pass

# print(type(Foo))
# print(type(Foo()))

## можно создать класс вручную
# Foo = type("Foo", (), {"x": 42})
# print(Foo.x)

class Meta(type):
    def __new__(mcs, name, bases, dct):
        # валидируем: все методы должны быть в snake_case
        for attr in dct:
            if callable(dct[attr]) and not attr.islower():
                raise TypeError(f'Метод {attr} должен быть в snake_case')
        return super().__new__(mcs, name, bases, dct)

class MyClass(metaclass = Meta):
    def valid_methods(self): pass
    # def BadMethod(self): pass #TypeError при определении класса