num1_TLD = float(input("Enter first number: "))
num2_TLD = float(input("Enter second number: "))

print("Addition:", num1_TLD + num2_TLD)
print("Subtraction:", num1_TLD - num2_TLD)
print("Multiplication:", num1_TLD * num2_TLD)

if num2_TLD != 0:
    print("Division:", num1_TLD / num2_TLD)
else:
    print("Division: Cannot divide by zero")