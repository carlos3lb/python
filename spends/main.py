from model.month import Month
from model.year import Year
from model.model import Model
import json


try:
    model = Model()
    model.load_spends('datos.csv')

    #Global:
    #Total
    #print("%.2f" % (model.get_total_by_type('total')))
    #Evolucion año actual
    print(model.get_monthly_ac_by_type_year('total', 2017))
    #evolucion entre años
    #Tabla gastos comparando mes actual vs media meses %
    #print((model.get_monthly_by_type_year('total', 2017)))
    #Tabla gastos medios vs actual %

    #Fide y comun:
    #Total
    #Evolucion año actual
    print(model.get_monthly_ac_by_type_owner_year('total', 'comun', 2017))
    #print((model.get_monthly_by_type_owner_year('total', 'fide', 2017)))
    #evolucion entre años


except Exception as ex:
    print("-- error --")  
    print(ex)  
