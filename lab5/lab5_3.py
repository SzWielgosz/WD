from typing import List


class Square:
    side: float

    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side**2

    def perimeter(self) -> float:
        return self.side*4


class Triangle:
    height: float
    base: float

    def __init__(self, base: float, height: float):
        self.height = height
        self.base = base

    def area(self) -> float:
        return (self.base * self.height)/2

    def perimeter(self) -> float:
        return self.base * 3


li1: List[any] = []
li2: List[any] = []
for i in range(11, 21):
    li1.append(Square(i))

for i in range(4):
    a: int = 6
    h: int = 15
    li2.append(Triangle(a, h))
    a += 1
    h += 1

for i in li1:
    print(Square.area(i), Square.perimeter(i))

for i in li2:
    print(Triangle.area(i), Triangle.perimeter(i))
