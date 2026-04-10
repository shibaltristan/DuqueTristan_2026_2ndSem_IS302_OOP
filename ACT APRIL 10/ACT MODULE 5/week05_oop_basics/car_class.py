class Cartld:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_carjt(self):
        print(self.brand, self.model, self.year)

car1tld = Cartld("Toyota", "Corolla", 2020)
car1tld.display_cartld()
