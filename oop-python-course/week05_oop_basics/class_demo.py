class Person:
    def __init__(self, name, age):
        self.name_TLD = name
        self.age_TLD = age

    def display_info(self):
        print("Name:", self.name_TLD)
        print("Age:", self.age_TLD)


p1 = Person("Juan", 20)
p1.display_info()
