"""
Una estructura condicional nos permite evaluar una condición.

la sintaxis es la siguiente:

if condición:
    instrucciones
else:
    otras instrucciones
----------------------------------------------------------------
Ejemplo 1:
Programa que verifica si un numero ingresado por teclado es par,
impar o cero.
----------------------------------------------------------------
"""
n = int(input("Ingresar un numero: "))

if n == 0:
    print("Es cero")
elif n % 2 == 0:
    print("Es par")
else:   print("Es impar")


