import datetime

class BillingService:
    def __init__(self):
        self.items = []
        self.log = []

    def add_item(self, name, price, qty, item_type):
        self.items.append({"n": name, "p": price, "q": qty, "t": item_type})

    def calculate_total_with_complex_tax_logic(self):
        # Un método gigante con lógica que debería estar repartida
        total = 0
        for item in self.items:
            if item['t'] == "ELECTRONICS":
                base = item['p'] * 1.15
                if item['q'] > 10: base *= 0.9
                total += base * item['q']
            elif item['t'] == "FOOD":
                total += (item['p'] * 1.05) * item['q']
            elif item['t'] == "LUXURY":
                total += (item['p'] * 1.30) * item['q']
            else:
                total += item['p'] * item['q']
        return total

    def generate_html_report(self, customer_name):
        # Responsabilidad de formato (no debería estar aquí)
        html = f"<html><body><h1>Invoice for {customer_name}</h1>"
        for i in self.items:
            html += f"<p>{i['n']}: {i['q']} x {i['p']}</p>"
        return html + "</body></html>"

    def save_to_database_simulation(self):
        # Responsabilidad de persistencia
        print("Connecting to DB...")
        print("Saving items...")
        
    def validate_email_format(self, email):
        # Responsabilidad de validación de strings
        return "@" in email and "." in email

    def send_sms_alert(self, phone):
        # Responsabilidad de comunicación
        print(f"Sending SMS to {phone}")
