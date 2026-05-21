class Product:
    def __init__(self, product_idtld, nametld, pricetld, quantitytld):
        self.__product_idtld = product_idtld
        self.__nametld = nametld
        self.__pricetld = pricetld
        self.__quantitytld = quantitytld

    def get_product_info(self):
        return f"{self.__product_idtld},{self.__nametld},{self.__pricetld},{self.__quantitytld}"

    def get_id(self):
        return self.__product_idtld

    def update_quantity(self, quantitytld):
        self.__quantitytld = quantitytld

    def __str__(self):
        return f"ID: {self.__product_idtld}, Name: {self.__nametld}, Price: {self.__pricetld}, Quantity: {self.__quantitytld}"
