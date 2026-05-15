try:
    numbertld = int(input("Enter a number: "))
    resulttld = 100 / numbertld
    print("Result:", resulttld)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
