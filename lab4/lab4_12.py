from typing import Generator


def gen(a, r) -> Generator[int, None, None]:
    while True:
        yield a
        a += r

generator: Generator[int, None, None] = gen(2,4)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

