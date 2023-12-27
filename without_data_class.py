class Investor:
    

    def __init__(self, name: str, age: int, cash: float):
        self.name = name
        self.age = age
        self.cash = cash

    def __repr__(self):
        return f"Name: {self.name}"
    
    def __eq__(self, other):
        return(self.name == other.name)

    def __lt__(self, other):
        return self.cash < other.cash

i1 = Investor("john", 25, 900)
i2 = Investor("Abir", 26, 13000)
i3 = Investor("Abit", 27, 1200)
i4 = Investor("john", 25, 1900)

print(i1 == i4)