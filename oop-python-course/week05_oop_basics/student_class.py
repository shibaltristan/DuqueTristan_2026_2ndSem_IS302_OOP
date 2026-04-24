class Student:
    def __init__(self, name, student_id, course):
        self.name_TLD = name
        self.student_id_TLD = student_id
        self.course_TLD = course

    def display_student(self):
        print("Name:", self.name_TLD)
        print("Student ID:", self.student_TLD)
        print("Course:", self.course_TLD)


student1 = Student("Maria", "2023-001", "BSIS")
student1.display_student()
