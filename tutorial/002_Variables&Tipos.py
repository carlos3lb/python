# Qué es una variable?
# Qué es un tipo?
# Python es un lenguaje orientado a objetos
# No es necesario declarar una variable antes de usarla o indicar su tipo

# Números (integer y float)
myint = 7
print(myint)

myfloat = 7.0
print(myfloat)

print(myfloat)
print(myint+float("7.2"))

# Textos (strings)

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

# Ejercicio: pintar un mensaje utilizando apostrofes (ingles)
print("I'm pretty")

# Operador +
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# Ejericio: pintar el mensaje hello world con dos variables utilizando el separador de la funcion print.
print(hello, world, " ")
# Ejercicio: funcionaría sumar variables con números y textos? y sin variables (1 + "texto")?
# print(hello + one)
# print("Cris" + 5)

# Declarar variables de forma simultanea
a, b = 3, 4
print(a,b)

# Ejercicio: funcionaría con tipos distintos?
a, b = 3, "casa"
print(a, b)