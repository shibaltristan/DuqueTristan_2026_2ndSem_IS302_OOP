def load_userstld(filenametld):
    userstld = {}
    try:
        with open(filenametld, "r") as filetld:
            for linetld in filetld:
                linetld = linetld.strip()
                if linetld:
                    partstld = linetld.split(",")
                    if len(partstld) == 2:
                        usernametld, passwordtld = partstld
                        userstld[usernametld.strip()] = passwordtld.strip()
    except FileNotFoundError:
        print("User data file not found.")
    return userstld


def maintld():
    userstld = load_userstld("users.txt")
    if not userstld:
        print("No users available for login.")
        return

    try:
        usernametld = input("Enter username: ").strip()
        passwordtld = input("Enter password: ").strip()
    except Exception:
        print("Error reading input. Please try again.")
        return

    if usernametld in userstld and userstld[usernametld] == passwordtld:
        print("Login successful")
    else:
        print("Invalid username or password")


if __name__ == "__main__":
    maintld()
