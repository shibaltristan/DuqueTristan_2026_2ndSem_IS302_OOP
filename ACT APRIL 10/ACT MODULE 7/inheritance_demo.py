class Animaltld:
    def __init__(self, nametld):
        self.nametld = nametld

    def speak(self):
        print(self.nametld, "makes a sound")

class Dogtld(Animaltld):
    def bark(self):
        print(self.nametld, "barks")

dog1tld = Dogtld("Buddy")
dog1tld.speak()
dog1tld.bark()