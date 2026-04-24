class Vehicletld:
    def __init__(self, brandtld, modeltld):
        self.brandtld = brandtld
        self.modeltld = modeltld

class Cartld(Vehicletld):
    def __init__(self, brandtld, modeltld, yeartld):
        super().__init__(brandtld, modeltld)
        self.yeartld = yeartld

    def display_cartld(self):
        print(self.brandtld, self.modeltld, self.yeartld)

car1tld = Cartld("Toyota", "Corolla", 2022)
car1tld.display_cartld()