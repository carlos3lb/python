from .month import Month
import json

# Year: clase para almacenar los gastos de un año
class Year:

    months = {}

    # Constructor 
    def __init__(self):
        self.months = {
            '1' : Month(),
            '2' : Month(),
            '3' : Month(),
            '4' : Month(),
            '5' : Month(),
            '6' : Month(),
            '7' : Month(),
            '8' : Month(),
            '9' : Month(),
            '10' : Month(),
            '11' : Month(),
            '12' : Month()
        }
    # ----

    # Metodo recuperar los gastos del año en funcion del tipo
    def spends_by_type(self, type):
        total = 0
        for k,month in self.months.items():
            total += month.get_spend(type)
        return total
    # ----

        # Metodo recuperar los gastos del mes del año en funcion del tipo
    def spends_by_month_type(self, month, type):
        return self.months[str(month)].get_spend(type)
    # ----

    # Metodo recuperar los gastos de un mes    
    def insert_spend(self, month, type, value):
        self.months[str(month)].insert_spend(type, value)
    # ----