class Person_TLD:
    def __init__(self_TLD, name_TLD, age_TLD):
        self_TLD.name_TLD = name_TLD
        self_TLD.age_TLD = age_TLD

    def display_info_TLD(self_TLD):
        print("Name:", self_TLD.name_TLD)
        print("Age:", self_TLD.age_TLD)

class Student_TLD(Person_TLD):
    def __init__(self_TLD, name_TLD, age_TLD, course_TLD):
        super().__init__(name_TLD, age_TLD)
        self_TLD.course_TLD = course_TLD

    def display_info_TLD(self_TLD):
        super().display_info_TLD()
        print("Course:", self_TLD.course_TLD)

class Teacher_TLD(Person_TLD):
    def __init__(self_TLD, name_TLD, age_TLD, subject_TLD):
        super().__init__(name_TLD, age_TLD)
        self_TLD.subject_TLD = subject_TLD

    def display_info_TLD(self_TLD):
        super().display_info_TLD()
        print("Subject:", self_TLD.subject_TLD)

# Example usage
student_TLD = Student_TLD("Maria", 20, "BSIS")
teacher_TLD = Teacher_TLD("Mr. Smith", 45, "Mathematics")

print("Student Info:")
student_TLD.display_info_TLD()
print("\nTeacher Info:")
teacher_TLD.display_info_TLD()