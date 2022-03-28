from typing import List
ma: List[List[int]] = [[]]
x: int = int(input("Podaj dlugosc macierzy:"))
for i in range(x):
    a = input(f"Podaj parametry {i+1} wiersza macierzy")
    ma.append(a)
print(ma)
