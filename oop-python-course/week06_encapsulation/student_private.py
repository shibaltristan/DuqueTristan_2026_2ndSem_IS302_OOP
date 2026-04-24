class Student_TLD:
    def __init__(self_TLD, name_TLD, student_id_TLD, gpa_TLD):
        self_TLD.__name_TLD = name_TLD
        self_TLD.__student_id_TLD = student_id_TLD
        self_TLD.__gpa_TLD = gpa_TLD

    def get_student_info_TLD(self_TLD):
        print("Name:", self_TLD.__name_TLD)
        print("Student ID:", self_TLD.__student_id_TLD)
        print("GPA:", self_TLD.__gpa_TLD)

student1_TLD = Student_TLD("Juan", "2023-001", 1.75)
student1_TLD.get_student_info_TLD()