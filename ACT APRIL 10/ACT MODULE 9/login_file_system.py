def registertld():
    usernametld = input("Enter username: ")
    passwordtld = input("Enter password: ")
    with open("users.txt", "a") as filetld:
        filetld.write(usernametld + "," + passwordtld + "\n")
    print("User registered successfully")

def logintld():
    usernametld = input("Enter username: ")
    passwordtld = input("Enter password: ")
    with open("users.txt", "r") as filetld:
        for linetld in filetld:
            stored_usernametld, stored_passwordtld = linetld.strip().split(",")
            if stored_usernametld == usernametld and stored_passwordtld == passwordtld:
                print("Login successful")
                return
    print("Invalid credentials")

while True:
    print("1 Register")
    print("2 Login")
    print("3 Exit")
    choicetld = input("Choose an option: ")
    if choicetld == "1":
        registertld()
    elif choicetld == "2":
        logintld()
    elif choicetld == "3":
        break
    else:
        print("Invalid choice")