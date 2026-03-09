class Product:
    def __init__(self, n, p, t, desc=""):
        self.name = n # Nombre poco descriptivo
        self.price = p
        self.type = t # 0, 1, 2...
        self.description = desc
        self.internal_id = "PROD-999" # Hardcoded
        self.temp_val = 0 # Campo inútil

class InvoiceItem:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.total_item = 0 # Esto debería ser un método, no un atributo
