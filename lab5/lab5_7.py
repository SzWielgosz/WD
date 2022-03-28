from typing import Iterator


def czy_pierwsza(x: int):
    if x == 2:
        return True
    else:
        y = 2
        while y < x:
            if x % y == 0:
                return False
            y += 1
    return True


class PrimeNumbers:
    x: int

    def __iter__(self) -> Iterator[int]:
        self.x = 2

        return self

    def __next__(self) -> int:
        result: int = self.x
        while True:
            if czy_pierwsza(result) is True:
                return self.x
            else:
                self.x += 1
                continue


iter_obj: PrimeNumbers = PrimeNumbers()
iterator: Iterator = iter(iter_obj)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

