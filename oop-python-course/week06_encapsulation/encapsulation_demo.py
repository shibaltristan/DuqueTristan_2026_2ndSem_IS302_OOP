class Person_TLD:
    def __init__(self_TLD, name_TLD, age_TLD):
        self_TLD.__name_TLD = name_TLD
        self_TLD.__age_TLD = age_TLD

    def get_name_TLD(self_TLD):
        return self_TLD.__name_TLD

    def get_age_TLD(self_TLD):
        return self_TLD.__age_TLD

p1_TLD = Person_TLD("Maria", 20)
print("Name:", p1_TLD.get_name_TLD())
print("Age:", p1_TLD.get_age_TLD())