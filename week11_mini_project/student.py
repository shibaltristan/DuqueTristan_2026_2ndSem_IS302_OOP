class Student:
    def __init__(self, student_idtld, nametld, coursetld):
        self.student_idtld = student_idtld
        self.nametld = nametld
        self.coursetld = coursetld

    def display_info(self):
        print(f"{self.student_idtld} | {self.nametld} | {self.coursetld}")

    def to_record(self):
        return f"{self.student_idtld},{self.nametld},{self.coursetld}\n"