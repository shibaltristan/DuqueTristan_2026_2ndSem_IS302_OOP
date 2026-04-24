class Vehicle_TLD:
    def __init__(self_TLD, brand_TLD, model_TLD):
        self_TLD.brand_TLD = brand_TLD
        self_TLD.model_TLD = model_TLD

class Car_TLD(Vehicle_TLD):
    def __init__(self_TLD, brand_TLD, model_TLD, year_TLD):
        super().__init__(brand_TLD, model_TLD)
        self_TLD.year_TLD = year_TLD

    def display_car_TLD(self_TLD):
        print(self_TLD.brand_TLD, self_TLD.model_TLD, self_TLD.year_TLD)

car1_TLD = Car_TLD("Toyota", "Corolla", 2022)
car1_TLD.display_car_TLD()