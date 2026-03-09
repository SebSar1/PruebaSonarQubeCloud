from models import Product, InvoiceItem
from billing_processor import BillingSystem

def main():
    s = BillingSystem()
    
    # Creamos objetos con nombres de variables horribles
    aaa = Product("Laptop", 1000, 0)
    bbb = Product("Vino", 50, 1)
    
    i1 = InvoiceItem(aaa, 1)
    i2 = InvoiceItem(bbb, 2)
    
    # Llamada con demasiados parámetros y tipos inconsistentes c
    res = s.process_everything("Juan", "Calle 1", "j@m.com", [i1, i2], "PROMO10", "USD", None, False)
    
    print(f"Resultado: {res}")
    
    # Forzar un posible error que Sonar detectará:
    # Division por cero o acceso a variable inexistente
    x = 10 / 0 if res < 0 else 1 

if __name__ == "__main__":
    main()

