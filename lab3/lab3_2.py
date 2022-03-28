from typing import List

li: List[int] = []
while True:
    try:
        x: int = int(input("Podaj liczbe calkowita:"))
        if x in li:
            print("Koniec")
            break
        else:
            li.append(x)
        print(li)
    except ValueError:
        print("To nie jest liczba calkowita!")
