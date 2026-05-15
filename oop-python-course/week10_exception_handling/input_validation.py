while True:
    try:
        numbertld = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
print("Valid number entered:", numbertld)
