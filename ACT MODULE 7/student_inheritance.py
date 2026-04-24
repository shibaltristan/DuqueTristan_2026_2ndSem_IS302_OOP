class Persontld:
    def __init__(self, nametld, agetld):
        self.nametld = nametld
        self.agetld = agetld

class Studenttld(Persontld):
    def __init__(self, nametld, agetld, coursetld):
        super().__init__(nametld, agetld)
        self.coursetld = coursetld

    def display_studenttld(self):
        print("Name:", self.nametld)
        print("Age:", self.agetld)
        print("Course:", self.coursetld)

student1tld = Studenttld("Maria", 20, "BSIS")
student1tld.display_studenttld()