from student import Student
from file_handler import save_student, view_students, search_student_by_id


def get_required_input(prompttld):
    while True:
        valuetld = input(prompttld).strip()
        if valuetld:
            return valuetld
        print("This field is required. Please enter a value.")


def add_student():
    student_idtld = get_required_input("Enter Student ID: ")
    nametld = get_required_input("Enter Name: ")
    coursetld = get_required_input("Enter Course: ")
    studenttld = Student(student_idtld, nametld, coursetld)
    save_student(studenttld)
    print("Student added successfully.")


def search_student():
    search_idtld = get_required_input("Enter Student ID to search: ")
    studenttld = search_student_by_id(search_idtld)
    if studenttld:
        print("Student Found:")
        studenttld.display_info()
    else:
        print("Student not found.")


def show_menu():
    print("\nSTUDENT INFORMATION SYSTEM")
    print("1 Add Student")
    print("2 View Students")
    print("3 Search Student")
    print("4 Exit")


if __name__ == "__main__":
    while True:
        show_menu()
        choicetld = input("Enter choice: ").strip()
        if choicetld == "1":
            add_student()
        elif choicetld == "2":
            view_students()
        elif choicetld == "3":
            search_student()
        elif choicetld == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")