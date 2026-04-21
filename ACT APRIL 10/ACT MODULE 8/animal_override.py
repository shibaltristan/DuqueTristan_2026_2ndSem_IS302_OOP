class Animaltld:
    def speak(self):
        print("Animal makes a sound")

class Dogtld(Animaltld):
    def speak(self):
        print("Dog barks")

class Cattld(Animaltld):
    def speak(self):
        print("Cat meows")

animalstld = [Dogtld(), Cattld()]
for animaltld in animalstld:
    animaltld.speak()