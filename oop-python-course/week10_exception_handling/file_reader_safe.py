try:
    with open("data.txt", "r") as filetld:
        contenttld = filetld.read()
        print(contenttld)
except FileNotFoundError:
    print("File does not exist")
