from product import Product

PRODUCT_FILE_TLD = "products.txt"


def add_product(producttld):
    with open(PRODUCT_FILE_TLD, "a") as file:
        file.write(producttld.get_product_info() + "\n")


def view_products():
    try:
        with open(PRODUCT_FILE_TLD, "r") as file:
            lines = [line.strip() for line in file if line.strip()]
            if not lines:
                print("No products found.")
                return
            print("\nCurrent Products:")
            for line in lines:
                data = [field.strip() for field in line.split(",")]
                print(f"ID: {data[0]}, Name: {data[1]}, Price: {data[2]}, Quantity: {data[3]}")
    except FileNotFoundError:
        print("No products found.")


def search_product(product_idtld):
    try:
        with open(PRODUCT_FILE_TLD, "r") as file:
            for line in file:
                data = [field.strip() for field in line.strip().split(",")]
                if data[0] == product_idtld:
                    return Product(data[0], data[1], float(data[2]), int(data[3]))
    except FileNotFoundError:
        return None
    return None


def update_quantity(product_idtld, new_quantitytld):
    try:
        updated = False
        products = []
        with open(PRODUCT_FILE_TLD, "r") as file:
            for line in file:
                if not line.strip():
                    continue
                data = [field.strip() for field in line.strip().split(",")]
                if data[0] == product_idtld:
                    products.append(f"{data[0]},{data[1]},{data[2]},{new_quantitytld}\n")
                    updated = True
                else:
                    products.append(line)
        if not updated:
            return False
        with open(PRODUCT_FILE_TLD, "w") as file:
            file.writelines(products)
        return True
    except FileNotFoundError:
        return False
