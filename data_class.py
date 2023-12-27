from dataclasses import dataclass, field

@dataclass(order=True, unsafe_hash = True)
class Investor:
    sort_index: float = field(init=False, repr=False)
    name: str
    age: int
    cash: float
    favoriteSport: str = field(repr = False, default="Soccer", hash = False)

    def __post_init__(self):
        self.sort_index = self.cash

i1 = Investor("john", 25, 900, "Soccer")
i2 = Investor("Abir", 26, 13000, "Basketball")
i3 = Investor("Abit", 27, 1200, "Cricket")
i4 = Investor("john", 25, 900)

mylist = [i1, i2, i3, i4]
mylist.sort()
print(mylist)
print(hash(i1))
print(hash(i4))
print(hash(i3))