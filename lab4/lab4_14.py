from typing import Generator


def czy_pierwsza(liczba) -> bool:
    for i in range(2, liczba - 1):
        if liczba % i == 0:
            return False
    return True


def gen() -> Generator[int, None, None]:
    x = 2
    while True:
        if czy_pierwsza(x):
            yield x
        x += 1



generator: Generator[int, None, None] = gen()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
