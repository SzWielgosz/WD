from typing import Generator


def gen(x) -> Generator[int, None, None]:
    if x % 2 == 1:
        x += 1
    while True:
        yield x
        x += 2


generator: Generator[int, None, None] = gen(10)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
