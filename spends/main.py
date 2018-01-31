from model.month import Month
from model.year import Year
from model.model import Model
import json


try:
    model = Model()
    model.load_spends('datos.csv')

    a = model.personal[2017].spends_by_type('casa')
    b = model.personal[2016].spends_by_type('casa')
    print("%.2f" % (a+b))

except Exception as ex:
    print("-- error --")  
    print(ex)  
