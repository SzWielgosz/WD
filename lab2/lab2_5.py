import math

r: float = float(input("Podaj promien kola:"))

pole: float = math.pi * r ** 2
print("Pole kola wynosi:", round(pole, 2))

obwod: float = 2 * math.pi * r
print("Obwod kola wynosi:", round(obwod, 2))
