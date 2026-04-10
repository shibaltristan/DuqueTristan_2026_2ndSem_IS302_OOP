correct_usernametld = "admin"
correct_passwordtld = "1234"
attemptstld = 0

while attemptstld < 3:
    userNametld = input("Enter username: ")
    passwordtld = input("Enter password: ")
    
    if userNametld == correct_usernametld and passwordtld == correct_passwordtld:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attemptstld += 1

if attemptstld == 3:
    print("Account Locked")