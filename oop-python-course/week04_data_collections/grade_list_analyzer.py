grades_TLD = []
for i in range(1, 6):
    grade = float(input(f"Enter grade {i}: "))
    grades_TLD.append(grade)

average = sum(grades_TLD) / len(grades_TLD)
highest = max(grades_TLD)
lowest = min(grades_TLD)

print(f"Average Grade: {average:.1f}")
print(f"Highest Grade: {highest}")
print(f"Lowest Grade: {lowest}")
