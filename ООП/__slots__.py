##============================================================ __slots__
class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(10, 20)
print(p.x) # ok
# p.z = 30 AttributeError