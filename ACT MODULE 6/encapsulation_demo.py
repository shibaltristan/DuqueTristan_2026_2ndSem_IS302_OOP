class Persontld:
    def __init__(self, nametld, agetld):
        self.__nametld = nametld
        self.__agetld = agetld

    def get_nametld(self):
        return self.__nametld

    def get_agetld(self):
        return self.__agetld

p1tld = Persontld("Maria", 20)
print("Name:", p1tld.get_nametld())
print("Age:", p1tld.get_agetld())