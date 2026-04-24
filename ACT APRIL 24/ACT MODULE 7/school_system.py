class Persontld:
    def __init__(self, nametld, agetld):
        self.nametld = nametld
        self.agetld = agetld

    def display_infotld(self):
        print("Name:", self.nametld)
        print("Age:", self.agetld)

class Studenttld(Persontld):
    def __init__(self, nametld, agetld, coursetld):
        super().__init__(nametld, agetld)
        self.coursetld = coursetld

    def display_infotld(self):
        super().display_infotld()
        print("Course:", self.coursetld)

class Teachertld(Persontld):
    def __init__(self, nametld, agetld, subjecttld):
        super().__init__(nametld, agetld)
        self.subjecttld = subjecttld

    def display_infotld(self):
        super().display_infotld()
        print("Subject:", self.subjecttld)

# Example usage
studenttld = Studenttld("Maria", 20, "BSIS")
studenttld.display_infotld()

teachertld = Teachertld("Mr. Smith", 35, "Mathematics")
teachertld.display_infotld()