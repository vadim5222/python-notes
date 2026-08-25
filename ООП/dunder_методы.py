#===================================================== Строковые представления: __str__, __repr__
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

#========================================================== Сравнения: __eq__, __it__, __gt__
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


#=======================================================Хещ: __hash__

# class Point:
#     def __init__(self, x, y):
#         self.x, self.y = x, y

#     def __eq__(self, other):
#         return (self.x, self.y) == (other.x, other.y)

#     def __hash__(self):
#         return hash((self.x, self.y))

# points = {Point(1,2), Point(1,2), Point(3,4)}
# print(len(points))