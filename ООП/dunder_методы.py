## ===================================================== Строковые представления: __str__, __repr__
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f'({self.x}, {self.y})'

#     def __repr__(self):
#         return f'Point(x={self.x}, y={self.y})'

# p = Point(3, 4)
# print(p)
# print(repr(p))

# #========================================================== Сравнения: __eq__, __it__, __gt__
# class Money:
#     def __init__(self, amount):
#         self.amount = amount

#     def __eq__(self, other):
#         return self.amount == other.amount

#     def __lt__(self, other):
#         return self.amount < other.amount

# a, b, c = Money(100), Money(100), Money(200)
# print(a == b)
# print(a < c)


# #=======================================================Хеш: __hash__

# class Point:
#     def __init__(self, x, y):
#         self.x, self.y = x, y

#     def __eq__(self, other):
#         return (self.x, self.y) == (other.x, other.y)

#     def __hash__(self):
#         return hash((self.x, self.y))

# points = {Point(1,2), Point(1,2), Point(3,4)}
# print(len(points))


# ===============================================Арифметика __add__, __sub__, __mul__
# class Vector:
#     def __init__(self, x, y):
#         self.x, self.y = x, y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def __mul__(self, k):
#         return Vector(self.x * k, self.y * k)

#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'

# v = Vector(1,2) + Vector(3, 4)
# print(v)
# print(v * 2)

## ========================================================Длина, итерация,  индексация
# class Playlist:
#     def __init__(self, songs):
#         self._songs = songs

#     def __len__(self):
#         return len(self._songs)

#     def __getitem__(self, i):
#         return self._songs[i]

#     def __iter__(self):
#         return iter(self._songs)

#     def __contains__(self, song):
#         return song in self._songs

# p = Playlist(['a', 'b', 'c'])
# print(len(p))
# print(p[1])
# for song in p:
#     print(song)
# print('b' in p)

## ==========================================================================Вызов обьекта как функции: __call__
# class Multiplier:
#     def __init__(self, factor):
#         self.factor = factor

#     def __call__(self, x):
#         return x * self.factor

# double = Multiplier(2)
# print(double(5))

## ====================================================Контекст-менеджеры: __enter__ / __exit__

# class Timer:
#     def __enter__(self):
#         import time
#         self.start = time.monotonic()
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         import time
#         print(f'Заняло {time.monotonic() - self.start:.2f}s')

# with Timer():
#     sum(range(10_000_000))



