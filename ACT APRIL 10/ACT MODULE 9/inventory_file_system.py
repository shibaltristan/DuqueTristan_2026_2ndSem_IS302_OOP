producttld = input("Enter product name: ")
pricetld = input("Enter price: ")
with open("inventory.txt", "a") as filetld:
    filetld.write(producttld + "," + pricetld + "\n")
print("Product saved successfully")