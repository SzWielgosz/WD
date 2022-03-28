def funkcja(a, b, c):
    print(f"Funkcja {a}x^2+{b}x+{c}")
    delta: float = b**2 - 4*a*c
    if delta > 0:
        pierwiastek = delta ** (1 / 2)
        x1: float = (-b-pierwiastek)/(2*a)
        x2: float = (-b+pierwiastek)/(2*a)
        return x1, x2
    elif delta == 0:
        x0: float = -b/(2*a)
        return x0
    else:
        return 0


print(funkcja(2, 6, 4))
