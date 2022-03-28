import math

r: float = float(input("Podaj promien kuli:"))

pole: float = 4 * math.pi * r ** 2
print("Pole wynosi:", round(pole, 2))

objetosc: float = 4/3 * math.pi * r ** 3
print("Objetosc wynosi:", round(objetosc, 2))
