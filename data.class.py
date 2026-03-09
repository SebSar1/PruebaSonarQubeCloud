class CustomerData:
    def __init__(self):
        # Una Data Class pura: solo campos, cero métodos de lógica.
        self.customer_id = 0
        self.full_name = ""
        self.email_address = ""
        self.shipping_address = ""
        self.is_premium = False
        self.total_spent = 0.0
        self.last_order_date = None
        self.tax_id = ""
