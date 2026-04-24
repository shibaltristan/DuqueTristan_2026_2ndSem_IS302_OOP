class Producttld:
    def __init__(self, nametld, pricetld, quantitytld):
        self.__nametld = nametld
        self.__pricetld = pricetld
        self.__quantitytld = quantitytld

    def get_product_infotld(self):
        print("Product:", self.__nametld)
        print("Price:", self.__pricetld)
        print("Quantity:", self.__quantitytld)

    def update_quantitytld(self, new_quantitytld):
        self.__quantitytld = new_quantitytld

    def update_pricetld(self, new_pricetld):
        self.__pricetld = new_pricetld

# Example usage
producttld = Producttld("Laptop", 45000, 10)
producttld.get_product_infotld()