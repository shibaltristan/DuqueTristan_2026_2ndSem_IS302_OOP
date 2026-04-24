name_TLD = input("Enter student name: ")
course_TLD = input("Enter course: ")
with open("students.txt", "a") as file_TLD:
    file_TLD.write(name_TLD + "," + course_TLD + "\n")

print("\nStudent Records")
with open("students.txt", "r") as file_TLD:
    for line_TLD in file_TLD:
        print(line_TLD.strip())
