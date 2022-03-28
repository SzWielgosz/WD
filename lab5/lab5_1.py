class Square:
    side: float

    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side**2

    def perimeter(self) -> float:
        return self.side*4


Square1: Square = Square(10)
print(Square1.area())
