"""
Operadores Lógicos: Permiten realizar varias comparaciones en una expresión lógica.
|-----------|-------------------|----------------------------------------------|
|  Operador |    Descripción    | Forma de utilización                         | 
|-----------|-------------------|----------------------------------------------|
|  and (&)  | Conjunción Lógica | True cuando todas las condiciones se cumplen.|
|   or (|)  | Disyunción Lógica | False cuando ninguna condicionesse cumple.   |
|  XOR (^)  | O Exclusivo       | True solo cuando se cumple una condición.    |
|    not    | No Lógico         | True cuando todas las condiciones se cumplen |
|-----------|-------------------|----------------------------------------------|
"""
# Verificar si un número es mayor a cero y menor que diez:
n = int(input("Ingresa un número: "))
bandera = False

if n > 0 and n < 10:
    bandera = True
else:
    bandera = False

print(bandera)

# Verificar si un número es mayor a 10 o menor a -10:
n = int(input("Ingresa otro número: "))
bandera = False

if n > 10 or n < -10:
    bandera = True
else:
    bandera = False

print(bandera)

if not bandera:
    print("Upss bandera esta negada...")

if n > -10 & n < 10:
    print(f"El valor era {n}")

if n ^ 0: # En realidad este operador funciona como un !=
    print("Prueba XOR")