def register_TLD():
    username_TLD = input("Enter username: ")
    password_TLD = input("Enter password: ")
    with open("users.txt", "a") as file_TLD:
        file_TLD.write(username_TLD + "," + password_TLD + "\n")
    print("Registration successful!")

def login_TLD():
    username_TLD = input("Enter username: ")
    password_TLD = input("Enter password: ")
    try:
        with open("users.txt", "r") as file_TLD:
            for line_TLD in file_TLD:
                stored_user_TLD, stored_pass_TLD = line_TLD.strip().split(",")
                if username_TLD == stored_user_TLD and password_TLD == stored_pass_TLD:
                    print("Login successful!")
                    return
        print("Invalid credentials!")
    except FileNotFoundError:
        print("No users registered yet!")

def main_TLD():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice_TLD = input("Enter choice: ")
        
        if choice_TLD == "1":
            register_TLD()
        elif choice_TLD == "2":
            login_TLD()
        elif choice_TLD == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main_TLD()