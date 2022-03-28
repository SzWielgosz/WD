from typing import List


def parzyste_i_nie(lista: [List]):
    x: [List] = []
    y: [List] = []
    for i in lista:
        if i % 2 == 0:
            x.append(i)
        else:
            y.append(i)
    return x, y


liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
parzyste, nieparzyste = parzyste_i_nie(liczby)
print(f"Liczby parzyste{parzyste}, a liczby nieparzyste:{nieparzyste}")
