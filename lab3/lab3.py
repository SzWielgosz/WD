from typing import Set

s: Set[int] = set()
while len(s) < 10:
    try:
        x: int = int(input("Podaj liczbe:"))
        s.add(x)
    except ValueError:
        print("Wpisz liczbe!")
print(s)
