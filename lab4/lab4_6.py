def srednia(*x):
    wynik: float = 0
    for i in x:
        wynik += i
    wynik /= len(x)
    return wynik


print(srednia(1, 2, 3))