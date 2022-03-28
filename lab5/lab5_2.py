class Triangle:
    side: float
    base: float

    def __init__(self, side: float, base: float) -> None:
        self.side = side
        self.base = base

    def area(self):
        return (self.side + self.base)/2

    def perimeter(self):
        return self.side * 3
