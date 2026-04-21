nametld = input("Enter student name: ")
coursetld = input("Enter course: ")
with open("students.txt", "a") as filetld:
    filetld.write(nametld + "," + coursetld + "\n")
print("\nStudent Records")
with open("students.txt", "r") as filetld:
    for linetld in filetld:
        print(linetld.strip())