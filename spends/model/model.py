from .year import Year
import csv

# Model: clase para almacenar y gestionar el modelo
class Model:

    comun = {}
    personal = {}

    # Constructor 
    def __init__(self):
        self.comun = {}
        self.personal = {}
    # ----

    # Metodo para insertar un gasto
    def insert_spend(self, month, year, value, owner, type):
        if (owner == 'fide'):
            if year not in self.personal.keys():
                self.personal[year] = Year()
            self.personal[year].insert_spend(month, type, value)
        elif (owner == 'comun'):
            if year not in self.comun.keys():
                self.comun[year] = Year()
            self.comun[year].insert_spend(month, type, value)
        else:
            raise Exception("Error: Wrong owner")
    # ----

    # Metodo para cargar los gastos de un fichero
    def load_spends(self, filename):
        with open(filename) as f:
            csvreader = csv.reader(f)
            for line in csvreader:
                splited = line[0].split(';')
                self.insert_spend(
                    splited[0], 
                    int(splited[1]), 
                    float(splited[2]), 
                    splited[3], 
                    splited[4])
    # ----