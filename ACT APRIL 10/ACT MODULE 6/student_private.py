class Studenttld:
    def __init__(self, nametld, student_idtld, gpatld):
        self.__nametld = nametld
        self.__student_idtld = student_idtld
        self.__gpatld = gpatld

    def get_student_infotld(self):
        print("Name:", self.__nametld)
        print("Student ID:", self.__student_idtld)
        print("GPA:", self.__gpatld)

student1tld = Studenttld("Juan", "2023-001", 1.75)
student1tld.get_student_infotld()