try:
    num1tld = float(input("Enter first number: "))
    num2tld = float(input("Enter second number: "))
    resulttld = num1tld / num2tld
    print("Result:", resulttld)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid numeric input")
