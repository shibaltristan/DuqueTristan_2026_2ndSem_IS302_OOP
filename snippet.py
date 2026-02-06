class Person:
    def __init__(self, name, height_in_cm,age):
        self.name = name
        self.age = age
        self.height_in_cm = height_in_cm

    def speak(self):
        print(f"Hello! My name is {self.name}. I Am {self.age} years old.")

adam = Person("Adam", 103213,2020)
lovelace = Person("Lovelace", 2000,10032)
lucre = person = Person("Lucre", 3000,100)
lovelace.speak()
adam.speak()
lucre.speak()

