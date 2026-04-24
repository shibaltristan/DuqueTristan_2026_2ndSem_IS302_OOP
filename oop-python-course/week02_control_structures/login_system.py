correct_username = "tan"
correct_password = "1234"
attempts = 0

while attempts < 3:
    username_TLD = input("Enter username: ")
    password = input("Enter password: ")

    if username_TLD == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attempts += 1

if attempts == 3:
    print("Account Locked")
