from typing import Dict

sl: Dict[str, str] = {"Cebula": "Onion", "Ziemniak": "Potato", "Pomidor": "Tomato"}
while True:
    x: str = input("Podaj slowo:")
    if x == "end":
        break
    if x not in sl:
        y: str = input("Podaj tlumaczenie:")
        sl[x] = y
    else:
        print(sl[x])
print(sl)
