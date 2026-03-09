from models import Product, InvoiceItem
from billing_processor import BillingSystem

def run_app():
    # Setup de datos
    p1 = Product("Laptop Gamer", 1500, 0)
    p2 = Product("Reloj de Oro", 5000, 1)
    p3 = Product("Pan", 2, 2)
    
    item1 = InvoiceItem(p1, 1)
    item2 = InvoiceItem(p2, 1)
    item3 = InvoiceItem(p3, 10)
    
    sistema = BillingSystem()
    
    # Ejecución
    sistema.create_invoice("Alice", "Av. Siempre Viva 742", "alice@example.com", [item1, item3], "PROMO10")
    sistema.create_invoice("Bob", "Calle Falsa 123", "bob@example.com", [item2], "SUPER50")
    
    sistema.generate_report()

if __name__ == "__main__":
    run_app()