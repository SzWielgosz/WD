import math
x: float = float(input("Podaj liczbe x:"))
y: float = float(input("Podaj liczbe y:"))
z: float = float(input("Podaj liczbe z:"))

print((x + y / z) ** x - z)
print((math.sqrt(x) - x ** 1 / z) / (x ** 1 / z + z ** 1 / x))
print(math.pi / x - math.atan(y))
print((x ** 1/3) - (y ** math.pi)) / (z ** y / math.e ** 10)
print((math.sin(x) + math.cos(y) / math.sin(x) + math.sin(y)))
print(math.log(x, y))
