def calculate_averagetld(grades):
    return sum(grades) / len(grades)


def get_remarktld(averagegradetld):
    if averagegradetld >= 90:
        return "Excellent"
    elif averagegradetld >= 85:
        return "Very Good"
    elif averagegradetld >= 80:
        return "Good"
    elif averagegradetld >= 75:
        return "Fair"
    else:
        return "Failed"


grade1tld = float(input("Enter grade for Subject 1: "))
grade2tld = float(input("Enter grade for Subject 2: "))
grade3tld = float(input("Enter grade for Subject 3: "))

average_gradetld = calculate_averagetld([grade1tld, grade2tld, grade3tld])
remarktld = get_remarktld(average_gradetld)

print("\n----- GRADE PROCESSOR -----")
print("Average Grade:", round(average_gradetld, 2))
print("Remark:", remarktld)
