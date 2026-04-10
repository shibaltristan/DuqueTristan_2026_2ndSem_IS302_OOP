class Studenttld:
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course
    
    def display_studenttld(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Course:", self.course)

student1tld = Studenttld("Maria", "2023-001", "BSIS")
student1tld.display_studenttld()
