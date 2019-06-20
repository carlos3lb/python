# Escribir un programa python que lea un numero y devuelva el elemetno en dicha posicion de la serie de fibonacci
# ej: dado el 6 devolverá 8 ya que (0,1,1,2,3,5,8)

import time

nombre = input("Numero a calcular: ")


# Escibir función

# --------------------------------------

start = time.time() * 1000.0

# LLamar a la funcuón y pintar resultado

# --------------------------------------

end = time.time() * 1000.0
duration = end-start
print ("Tiempo total %0.0f ms" % duration)

# Ejercicio:  influir gráficos

# Sabiendo que un diccionario es un clave valor que podemos utilizar de esta manera, mejorar el algoritmo anterior:
# ej: 
#memoria = {"a":"letra a", "b":"letra b"}
#memoria["c"] = "letra c"
#try:
#    print(memoria["d"])
#except:
#    print(memoria["c"])