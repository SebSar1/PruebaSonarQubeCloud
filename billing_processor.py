import datetime
import os # Import no usado (Sonar lo detecta)

class BillingSystem:
    def __init__(self):
        self.invoices = []
        self.db_path = "C:/users/admin/documents/database.db" # Hardcoded Path

    def process_everything(self, client_name, address, email, items, discount, currency, tax_id, is_company):
        # Smell: Long Parameter List (Demasiados argumentos)
        
        total = 0
        print("Iniciando proceso...") # Side effect innecesario

        # Smell: Deep Nesting & High Cognitive Complexity
        if items is not None:
            if len(items) > 0:
                for item in items:
                    if item.p.type == 0:
                        tax = 1.21
                        total += (item.p.price * tax) * item.q
                    else:
                        if item.p.type == 1:
                            tax = 1.35
                            total += (item.p.price * tax) * item.q
                        else:
                            if item.p.type == 2:
                                total += (item.p.price * 1.10) * item.q
                            else:
                                total += item.p.price * item.q
            else:
                print("No hay items")
        
        # Smell: Magic Strings & Duplicated Logic
        if discount == "PROMO10":
            total = total - (total * 0.10)
        elif discount == "SUPER50":
            total = total - (total * 0.50)
        elif discount == "WELCOME":
            total = total - 5

        # Smell: Empty except (Bad practice)
        try:
            f = open("log.txt", "a")
            f.write("Factura creada")
            f.close()
        except:
            pass 

        invoice = {
            "c": client_name,
            "addr": address,
            "e": email,
            "t": total,
            "d": datetime.datetime.now()
        }
        
        self.invoices.append(invoice)
        return total

    def calculate_taxes_again(self):
        # Smell: Duplicated Code (Casi lo mismo que arriba)
        # Esto aumenta la deuda técnica
        t_recaudado = 0
        for i in self.invoices:
            # Aquí se repite la lógica de los IF de arriba de forma manual
            t_recaudado += i['t'] * 0.21 
        return t_recaudado

    def send_stuff(self, m):
        # Smell: Unused local variable
        unused_var = "Hola"
        print(f"Enviando... {m}")
