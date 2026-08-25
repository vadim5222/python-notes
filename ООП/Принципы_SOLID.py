## =================================================================S — Single Responsibility Principle (SRP)
## плохо: класс знает и про юзера и про базу и про email
class User:
    def save_to_db(self): ...
    def send_welcome_email(self): ...

## хорошо: разделяем
class User: ...
class UserRepository:
    def save(self, user): ...
class EmailService:
    def send_welcome(self, email): ...


## =================================================================== O — Open/Closed Principle (OCP)
## плохо
class PaymentProcessor:
    def process(self, kind, amount):
        if kind == 'card':
            ...
        elif kind == 'crypto':
            ...
        ## чтобы добавить paypal - правим существующий метод

## хорошо
class Payment(ABC):
    @abstractmethod
    def process(self, amount):
        ...

class CardPayment(Payment): ...
class CryptoPayment(Payment): ...
class PayPalPayment(Payment): ... ##добавили без изменения других классов

## =============================================================================== L — Liskov Substitution Principle (LSP)
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h

    def set_width(self, w):
        self.w = w

class Square(Rectangle):
    def set_width(self, w):
        self.w = w
        self.h = w #Square нарушает контракт: у Rectangle set_width не трогал height


## ==================================================================================== I — Interface Segregation Principle (ISP)
## плохо
class Worker(ABC):
    @abstractmethod
    def work(self): ...
    @abstractmethod
    def eat(self): ...

class Robot(Worker):
    def work(self): ...
    def eat(self): ... ## роботу не надо есть но обязан реализовать


# хорошо
class Workable(Protocol):
    def work(self): ...

class Eateble(Protocol):
    def eat(self): ...

## =============================================================================== D — Dependency Inversion Principle (DIP)
## плохо
class UserService:
    def __init__(self):
        self.db = PostgresDatabase()

##хорошо
class UserService:
    def __init__(self, db: Database):
        self.db = db
