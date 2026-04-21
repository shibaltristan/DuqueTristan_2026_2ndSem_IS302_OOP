class Dogtld:
    def speak(self):
        print("Dog barks")

class Cattld:
    def speak(self):
        print("Cat meows")

animalstld = [Dogtld(), Cattld()]
for animaltld in animalstld:
    animaltld.speak()