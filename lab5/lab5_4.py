class Tree:
    name: str
    height: float
    leafs: int

    def __init__(self, name: str, height: float, leafs: int) -> None:
        self.name = name
        self.height = height
        self.leafs = leafs

    def grow_up(self, x) -> float:
        self.height += x
        return self.height

    def grow_wide(self, x) -> int:
        self.leafs += x
        return self.leafs

    def show(self) -> None:
        print(f"Drzewo zwie sie {self.name}, ma {self.height}m wysokosci, oraz {self.leafs} lisci")


tree1: Tree = Tree("Jarzab maczny(Sorbus aria)", 10, 2000)
tree2: Tree = Tree("Dąb blotny(Quercus palustris)", 20, 3460)
tree3: Tree = Tree("Lipa drobnolistna(Tilia cordata)", 30, 6000)
tree4: Tree = Tree("Klon grabolistny(Acer carpinifolium)", 8, 1250)
tree5: Tree = Tree("Brzoza brodawkowata(Betula pendula)", 15, 2450)

tree1.show()
tree2.show()
tree3.show()
tree4.show()
tree5.show()

tree1.grow_up(2)
tree1.show()
tree2.grow_up(1.5)
tree2.show()
