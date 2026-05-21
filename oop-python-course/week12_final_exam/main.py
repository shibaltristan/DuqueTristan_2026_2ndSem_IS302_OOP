from product import Product
from inventory_manager import add_product, view_products, search_product, update_quantity


def get_float_input(prompt):
    while True:
        try:
            valuetld = float(input(prompt))
            if valuetld < 0:
                raise ValueError
            return valuetld
        except ValueError:
            print("Invalid number. Please enter a valid positive number.")


def get_int_input(prompt):
    while True:
        try:
            valuetld = int(input(prompt))
            if valuetld < 0:
                raise ValueError
            return valuetld
        except ValueError:
            print("Invalid integer. Please enter a valid positive integer.")


def add_product_menu():
    product_idtld = input("Enter Product ID: ").strip()
    nametld = input("Enter Product Name: ").strip()
    pricetld = get_float_input("Enter Price: ")
    quantitytld = get_int_input("Enter Quantity: ")
    producttld = Product(product_idtld, nametld, pricetld, quantitytld)
    add_product(producttld)
    print("Product added successfully")


def search_product_menu():
    product_idtld = input("Enter Product ID: ").strip()
    producttld = search_product(product_idtld)
    if producttld:
        print("Product Found:")
        print(producttld)
    else:
        print("Product not found")


def update_quantity_menu():
    product_idtld = input("Enter Product ID: ").strip()
    producttld = search_product(product_idtld)
    if not producttld:
        print("Product not found")
        return
    print("Current product:")
    print(producttld)
    new_quantitytld = get_int_input("Enter new quantity: ")
    if update_quantity(product_idtld, new_quantitytld):
        print("Quantity updated successfully")
    else:
        print("Failed to update quantity")


def main():
    while True:
        print("\nINVENTORY MANAGEMENT SYSTEM")
        print("1 Add Product")
        print("2 View Products")
        print("3 Search Product")
        print("4 Update Quantity")
        print("5 Exit")
        choice_tld = input("Enter choice: ").strip()
        if choice_tld == "1":
            add_product_menu()
        elif choice_tld == "2":
            view_products()
        elif choice_tld == "3":
            search_product_menu()
        elif choice_tld == "4":
            update_quantity_menu()
        elif choice_tld == "5":
            print("Exiting inventory management system.")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
