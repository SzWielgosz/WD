from typing import Generator

def gen() -> Generator[int, None, None]:
    n0 = 0
    n1 = 1
    n2 = n0 + n1
    while True:
        yield n2
        n0 = n1
        n1 = n2
        n2 = n0 + n1

generator: Generator[int, None, None] = gen()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))