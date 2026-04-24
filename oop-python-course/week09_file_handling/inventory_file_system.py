product_TLD = input("Enter product name: ")
price_TLD = input("Enter price: ")

with open("inventory.txt", "a") as file:
    file.write(product_TLD + "," + price_TLD + "\n")

print("Product saved successfully")