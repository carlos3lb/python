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

    # Metodo para recuperar el total de gastos
    def get_total_by_type_owner(self, type, owner):
        total = 0
        if (owner == 'fide'):
            for k,year in self.personal.items():
                total += self.get_total_by_type_owner_year(type, 'fide', k)
        elif (owner == 'comun'):
            for k,year in self.comun.items():
                total += self.get_total_by_type_owner_year(type, 'comun', k)
        else:
            raise Exception("Error: Wrong owner")
        return total
    # ----

    # Metodo para recuperar el total de gastos por tipo, dueño y año
    def get_total_by_type_owner_year(self, type, owner, year):
        if (owner == 'fide'):
            return self.personal[year].spends_by_type(type)
        elif (owner == 'comun'):
            return self.comun[year].spends_by_type(type)
        else:
            raise Exception("Error: Wrong owner")
    # ----

    # Metodo para recuperar el total de gastos por tipo, dueño y año
    def get_monthly_by_type_year(self, type, year):
        p = self.personal[year].monthly_spends_by_type(type)
        c = self.comun[year].monthly_spends_by_type(type)
        spends = []
        for i in range(0, 12): 
            spends.append(p[i] + c[i])
        return spends
    # ----

    # Metodo para recuperar el total de gastos por tipo, dueño y año
    def get_monthly_by_type_owner_year(self, type, owner, year):
        if (owner == 'fide'):
            return self.personal[year].monthly_spends_by_type(type)
        elif (owner == 'comun'):
            return self.comun[year].monthly_spends_by_type(type)
        else:
            raise Exception("Error: Wrong owner")
    # ----

    # Metodo para recuperar el total de gastos por tipo, dueño y año
    def get_monthly_ac_by_type_year(self, type, year):
        p = self.get_monthly_ac_by_type_owner_year(type, 'fide', year)
        c = self.get_monthly_ac_by_type_owner_year(type, 'comun', year)
        spends = []
        for i in range(0, 12): 
            spends.append(p[i] + c[i])
        return spends
    # ----

    # Metodo para recuperar el total de gastos por tipo, dueño y año
    def get_monthly_ac_by_type_owner_year(self, type, owner, year):
        ac = 0
        y = []
        if (owner == 'fide'):
            for i in range(2016, year):
                if i in self.personal:
                    ac += self.get_total_by_type_owner_year(type, owner, i)
            y = self.personal[year].monthly_spends_by_type(type)
            for i in range(0, 12): 
                y[i] += ac
                ac = y[i]
            return y
        elif (owner == 'comun'):
            for i in range(2016, year):
                if i in self.personal:
                    ac += self.get_total_by_type_owner_year(type, owner, i)
            y = self.comun[year].monthly_spends_by_type(type)
            for i in range(0, 12): 
                y[i] += ac
                ac = y[i]
            return y
        else:
            raise Exception("Error: Wrong owner")
    # ----

    

