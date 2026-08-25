# class Shape:
#     def area(self):
#         raise NotImplementedError

# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r

#     def area(self):
#         return 3.14 * self.r * 2

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# shapes = [Circle(5), Square(3)]
# for s in shapes:
#     print(s.area())