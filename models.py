class Product:
    def __init__(self, name, price, product_type):
        self.name = name
        self.price = price
        # 0: Normal, 1: Lujo, 2: Esencial
        # Smell: Primitive Obsession
        self.product_type = product_type 

class InvoiceItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity