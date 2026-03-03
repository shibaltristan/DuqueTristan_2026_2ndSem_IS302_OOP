from person import Person

class Student(Person):
    def __init__ (self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def get_student_id(self):
        return self.student_id

    def get_course(self):
        return self.course

    # method overriding
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, ID: {self.student_id}, Course: {self.course}"

    def to_file_format(self):
        return f"{self.name},{self.age},{self.student_id},{self.course}\n"
