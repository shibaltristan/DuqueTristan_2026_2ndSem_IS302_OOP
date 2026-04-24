class Employeetld:
    def __init__(self, nametld):
        self.__nametld = nametld
        self.__salarytld = 0

    def set_salarytld(self, salarytld):
        if salarytld > 0:
            self.__salarytld = salarytld

    def get_salarytld(self):
        return self.__salarytld

emptld = Employeetld("Ana")
emptld.set_salarytld(30000)
print("Salary:", emptld.get_salarytld())