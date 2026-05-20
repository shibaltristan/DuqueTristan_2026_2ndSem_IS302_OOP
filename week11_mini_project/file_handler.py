from student import Student

STUDENT_FILETLD = "students.txt"


def save_student(studenttld):
    try:
        with open(STUDENT_FILETLD, "a", encoding="utf-8") as filetld:
            filetld.write(studenttld.to_record())
    except Exception as errtld:
        print("Error saving student:", errtld)


def view_students():
    try:
        with open(STUDENT_FILETLD, "r", encoding="utf-8") as filetld:
            print("\nSTUDENT LIST")
            print("ID | NAME | COURSE")
            print("-------------------")
            foundtld = False
            for lineld in filetld:
                student_idtld, nametld, coursetld = lineld.strip().split(",")
                studenttld = Student(student_idtld, nametld, coursetld)
                studenttld.display_info()
                foundtld = True
            if not foundtld:
                print("No student records found.")
    except FileNotFoundError:
        print("No records found.")
    except Exception as errtld:
        print("Error reading records:", errtld)


def search_student_by_id(search_idtld):
    try:
        with open(STUDENT_FILETLD, "r", encoding="utf-8") as filetld:
            for lineld in filetld:
                student_idtld, nametld, coursetld = lineld.strip().split(",")
                if student_idtld == search_idtld:
                    return Student(student_idtld, nametld, coursetld)
    except FileNotFoundError:
        return None
    except Exception:
        return None
    return None