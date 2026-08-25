from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1) # Point(x=1, y=2) - __repr__ сгенерирован
print(p1 == p2) # True

## Опции
# @dataclass(frozen=True, slots=True, kw_only=True)
# class Point:
#     x: int
#     y: int

from dataclasses import dataclass, field
@dataclass
class Team:
    name: str
    members: list = field(default_factory=list)