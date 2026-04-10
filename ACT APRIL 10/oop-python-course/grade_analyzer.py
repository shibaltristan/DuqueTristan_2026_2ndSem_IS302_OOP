student_nametld = input("Enter student name: ")

grade1tld = float(input("Enter grade for Subject 1: "))
grade2tld = float(input("Enter grade for Subject 2: "))
grade3tld = float(input("Enter grade for Subject 3: "))

average_gradetld = (grade1tld + grade2tld + grade3tld) / 3

if average_gradetld >= 90:
    remarktld = "Excellent"
elif average_gradetld >= 85:
    remarktld = "Very Good"
elif average_gradetld >= 80:
    remarktld = "Good"
elif average_gradetld >= 75:
    remarktld = "Fair"
else:
    remarktld = "Failed"

print("\n----- STUDENT GRADE ANALYZER -----")
print("Student Name:", student_nametld)
print("Average Grade:", round(average_gradetld, 2))
print("Remark:", remarktld)
