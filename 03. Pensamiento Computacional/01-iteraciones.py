"""
================================================================================
01 - ITERACIONES: Control de Flujo con Bucles
================================================================================

CONCEPTO:
---------
Las iteraciones permiten ejecutar un bloque de código múltiples veces.
En Python, usamos principalmente dos tipos de bucles:
- while: Se ejecuta mientras una condición sea verdadera
- for: Itera sobre una secuencia (listas, rangos, etc.)

CONTROL DE FLUJO:
-----------------
- break: Termina el bucle inmediatamente
- continue: Salta a la siguiente iteración
- else: Se ejecuta cuando el bucle termina normalmente (sin break)

EJEMPLO:
--------
Este programa cuenta del 0 al 9, pero se detiene si el contador supera 6.
================================================================================
"""

# Inicializamos el contador en 0
contador = 0

print("Iniciando el bucle while...\n")

# El bucle se ejecuta mientras contador < 10
while contador < 10:
    print(f"Valor actual del contador: {contador}")
    
    # Incrementamos el contador en 1
    contador += 1   # Equivalente a: contador = contador + 1
    
    # Si el contador supera 6, salimos del bucle
    if contador > 6:
        print("\n¡El contador superó 6! Saliendo del bucle con 'break'...")
        break

print("\nBucle terminado")
print(f"Valor final del contador: {contador}")

"""
================================================================================
EJERCICIOS PROPUESTOS:
================================================================================

1. Modifica el programa para que cuente del 1 al 20, pero que se salte 
   (usando 'continue') los números divisibles por 3.

2. Crea un bucle que sume todos los números del 1 al 100 y muestre el resultado.

3. Implementa un bucle que imprima la tabla de multiplicar del 7.

4. Crea un programa que pida números al usuario hasta que ingrese 0,
   y luego muestre la suma de todos los números ingresados.

================================================================================
ANÁLISIS:
================================================================================
Complejidad temporal: O(n) donde n es el número de iteraciones
Complejidad espacial: O(1) - Solo usamos una variable
================================================================================
"""
