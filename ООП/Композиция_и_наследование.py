class Car(Engine): # Car is an Engine  - звучит странно, потому что это неправда
    ...

class Car:
    def __init__(self):
        self.engine = Engine() # car has an engine - вот это уже логично

    def start(self):
        self.engine.start()