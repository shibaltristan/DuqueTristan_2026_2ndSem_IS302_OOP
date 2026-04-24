class Product_TLD:
    def __init__(self_TLD, name_TLD, price_TLD, quantity_TLD):
        self_TLD.__name_TLD = name_TLD
        self_TLD.__price_TLD = price_TLD
        self_TLD.__quantity_TLD = quantity_TLD

    def get_product_info_TLD(self_TLD):
        print("Product:", self_TLD.__name_TLD)
        print("Price:", self_TLD.__price_TLD)
        print("Quantity:", self_TLD.__quantity_TLD)

    def update_quantity_TLD(self_TLD, new_quantity_TLD):
        if new_quantity_TLD >= 0:
            self_TLD.__quantity_TLD = new_quantity_TLD

    def update_price_TLD(self_TLD, new_price_TLD):
        if new_price_TLD > 0:
            self_TLD.__price_TLD = new_price_TLD

# Example usage
product_TLD = Product_TLD("Laptop", 45000, 10)
product_TLD.get_product_info_TLD()