"""
Una función es un conjunto de instrucciones agrupadas bajo  un  nombre concreto que pueden reutilizarse invocando a la funcion tantas veces como sea necesario. 

----------------------------------------------------------------
def nombre_funcion(parametros):
    instrucciones

"""
# Funciones sin parámetros:
def saludar():
    print("Hola Mundo desde Python")

# Funciones con parámetros
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

n1 = int(input("Primer número: "))
n2 = int(input("Segundo número: "))

suma = sumar(n1, n2)
print("Suma: ", suma)
resta = restar(n1, n2)
print("Resta: ", resta)
producto = multiplicar(n1, n2)
print("Multiplicacion: ", producto)
cociente = dividir(n1, n2)
print("División: ", cociente)
