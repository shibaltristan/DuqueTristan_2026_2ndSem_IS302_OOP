gradestld = []

for itld in range(5):
    grade = float(input(f"Enter grade {itld + 1}: "))
    gradestld.append(grade)

average_gradetld = sum(gradestld) / len(gradestld)
highest_gradetld = max(gradestld)
lowest_gradetld = min(gradestld)

print("\nAverage Grade:", round(average_gradetld, 2))
print("Highest Grade:", highest_gradetld)
print("Lowest Grade:", lowest_gradetld)