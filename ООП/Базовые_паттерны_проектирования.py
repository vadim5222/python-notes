## =================================== Singleton

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

## ================================ Factory
class ShapeFactory:
    @staticmethod
    def create(kind, **kwargs):
        if kind == 'circle':
            return Circle(**kwargs)
        if kind == 'square':
            return Circle(**kwargs)
        raise ValueError(f'Unknown shape: {kind}')


## ============================================= Strategy
class SortStrategy(Porotocol):
    def sort(self, data):
        ...

class QuickSort:
    def sort(self, data):
        ...

class MergeSort:
    def sort(self, data):
        ...

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def run(self, data):
        return self.strategy.sort(data)

## =====================================Observer
class Publisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, fn):
        self.subscribers.append(fn)

    def publish(self, event):
        for fn in self.subscribers:
            fn(event)

## ======================================Reposiroty
class UserReposiroty:
    def get_by_id(self, user_id) -> None: ...
    def save(self, user: User) -> None: ...