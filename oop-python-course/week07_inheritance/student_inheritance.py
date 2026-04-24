class Person_TLD:
    def __init__(self_TLD, name_TLD, age_TLD):
        self_TLD.name_TLD = name_TLD
        self_TLD.age_TLD = age_TLD

class Student_TLD(Person_TLD):
    def __init__(self_TLD, name_TLD, age_TLD, course_TLD):
        super().__init__(name_TLD, age_TLD)
        self_TLD.course_TLD = course_TLD

    def display_student_TLD(self_TLD):
        print("Name:", self_TLD.name_TLD)
        print("Age:", self_TLD.age_TLD)
        print("Course:", self_TLD.course_TLD)

student1_TLD = Student_TLD("Maria", 20, "BSIS")
student1_TLD.display_student_TLD()