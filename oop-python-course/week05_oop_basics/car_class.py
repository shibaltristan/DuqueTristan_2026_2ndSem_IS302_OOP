class Car:
    def __init__(self, brand, model, year):
        self.brand_TLD = brand
        self.model_TLD = model
        self.year_TLD = year

    def display_car(self):
        print(self.brand_TLD, self.model_TLD, self.year_TLD)


car1 = Car("Toyota", "Corolla", 2020)
car1.display_car()
