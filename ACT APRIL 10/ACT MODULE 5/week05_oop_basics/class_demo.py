class Persontld:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_infotld(self):
        print("Name:", self.name)
        print("Age:", self.age)

p1tld = Persontld("Juan", 20)
p1tld.display_infotld()
