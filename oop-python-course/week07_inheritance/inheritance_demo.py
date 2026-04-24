class Animal_TLD:
    def __init__(self_TLD, name_TLD):
        self_TLD.name_TLD = name_TLD

    def speak(self_TLD):
        print(self_TLD.name_TLD, "makes a sound")

class Dog_TLD(Animal_TLD):
    def bark(self_TLD):
        print(self_TLD.name_TLD, "barks")

dog1_TLD = Dog_TLD("Buddy")
dog1_TLD.speak()
dog1_TLD.bark()