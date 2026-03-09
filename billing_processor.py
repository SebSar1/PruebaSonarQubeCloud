import datetime

class BillingSystem:
    def __init__(self):
        self.invoices = []

    # Smell: Long Parameter List & High Complexity
    def create_invoice(self, c_name, c_address, c_email, items, discount_code):
        total = 0
        for item in items:
            # Smell: Feature Envy & Switch Statements (if/elif)
            # La lógica de impuestos debería estar en Product, no aquí.
            if item.product.product_type == 0:
                total += (item.product.price * 1.21) * item.quantity
            elif item.product.product_type == 1:
                total += (item.product.price * 1.35) * item.quantity
            elif item.product.product_type == 2:
                total += (item.product.price * 1.10) * item.quantity
        
        # Smell: Hardcoded Values (Magic Strings/Numbers)
        if discount_code == "PROMO10":
            total = total * 0.9
        elif discount_code == "SUPER50":
            total = total * 0.5

        invoice_data = {
            "customer": c_name,
            "address": c_address,
            "email": c_email,
            "total": total,
            "date": datetime.datetime.now(),
            "items": items
        }
        
        self.invoices.append(invoice_data)
        
        # Smell: Violación de Single Responsibility Principle (SRP)
        # Esta clase gestiona datos, envía correos Y escribe archivos.
        self.send_email_notification(c_email, total)
        self.save_to_file(invoice_data)
        return invoice_data

    def send_email_notification(self, email, amount):
        print(f"Enviando correo a {email} por un monto de {amount}...")

    def save_to_file(self, data):
        with open("facturas_db.txt", "a") as f:
            f.write(f"{data['date']}: {data['customer']} - {data['total']}\n")

    def generate_report(self):
        print("--- REPORTE DE VENTAS ---")
        total_ventas = 0
        impuestos_totales = 0
        
        for inv in self.invoices:
            total_ventas += inv['total']
            # Smell: Code Duplication
            # Se repite la lógica de cálculo de impuestos que ya estaba en create_invoice
            for item in inv['items']:
                if item.product.product_type == 0:
                    impuestos_totales += (item.product.price * 0.21) * item.quantity
                elif item.product.product_type == 1:
                    impuestos_totales += (item.product.price * 0.35) * item.quantity
        
        print(f"Total: {total_ventas} | Impuestos: {impuestos_totales}")