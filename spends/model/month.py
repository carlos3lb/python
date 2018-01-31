import json

# MONTH: clase para almacenar los gastos de un mes
class Month:

    spends = {}
    
    # Constructor 
    def __init__(self):
        self.spends = {
            'cajero' : 0,
            'casa' : 0,
            'compraBasica' : 0,
            'compras' : 0,
            'cris' : 0,
            'fide' : 0,
            'ocio' : 0,
            'salario' : 0,
            'transferencia' : 0,
            'vacaciones' : 0,
            'total' : 0
        }
    # ----

    # Metodo para insertar un metodo a una categoria y acumular el total    
    def insert_spend(self, type, value):
        self.spends[type] += value
        self.spends['total'] += value
    # ----

    # Metodo recuperar los gastos de una categoria    
    def get_spend(self, type):
        return self.spends[type]
    # ----

    # Metodo recuperar los gastos de una categoria    
    def __str__(self):
        return str(self.spends)
    # ----


        