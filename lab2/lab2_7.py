import math

a: float = float(input("Podaj wspolczynnik a:"))
b: float = float(input("Podaj wspolczynnik b:"))
c: float = float(input("Podaj wspolczynnik c:"))

print(f"Twoja funkcja kwadratowa to {a}x^2+{b}x+{c}")

delta: float = b ** 2 - 4 * a * c

print("Delta wynosi:", delta)

if delta > 0:
    x1: float = (-b - math.sqrt(delta)) / (2 * a)
    x2: float = (-b + math.sqrt(delta)) / (2 * a)
    print(f"Dwa miejsca zerowe:x1 = {x1} , x2 = {x2}")
elif delta == 0:
    x0: float = -b / (2 * a)
    print(f"Jedno miejsce zerowe:x0 = {x0}")
else:
    print("Brak miejsc zerowych")
