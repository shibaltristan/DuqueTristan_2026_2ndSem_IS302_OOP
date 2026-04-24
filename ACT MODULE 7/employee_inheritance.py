class Employeetld:
    def __init__(self, nametld, salarytld):
        self.nametld = nametld
        self.salarytld = salarytld

class Managertld(Employeetld):
    def __init__(self, nametld, salarytld, departmenttld):
        super().__init__(nametld, salarytld)
        self.departmenttld = departmenttld

    def display_managertld(self):
        print("Name:", self.nametld)
        print("Salary:", self.salarytld)
        print("Department:", self.departmenttld)

manager1tld = Managertld("John", 50000, "IT")
manager1tld.display_managertld()