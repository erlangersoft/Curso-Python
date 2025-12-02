"""
================================================================================
02 - PROGRAMAS RAMIFICADOS: Toma de Decisiones
================================================================================

CONCEPTO:
---------
Los programas ramificados utilizan estructuras condicionales para tomar
decisiones y ejecutar diferentes bloques de código según las condiciones.

ESTRUCTURAS CONDICIONALES:
--------------------------
- if: Ejecuta un bloque si la condición es verdadera
- elif: (else if) Evalúa otra condición si la anterior fue falsa
- else: Se ejecuta si ninguna condición anterior fue verdadera

OPERADORES DE COMPARACIÓN:
--------------------------
- ==  : Igual a
- !=  : Diferente de
- >   : Mayor que
- <   : Menor que
- >=  : Mayor o igual que
- <=  : Menor o igual que

EJEMPLO:
--------
Este programa compara dos números enteros y determina cuál es mayor.
================================================================================
"""

print("=" * 60)
print("COMPARADOR DE NÚMEROS ENTEROS")
print("=" * 60)

# Solicitar al usuario que ingrese dos números
num_1 = int(input('\nEscoge un entero: '))
num_2 = int(input('Escoge otro entero: '))

print("\n" + "-" * 60)
print("RESULTADO:")
print("-" * 60)

# Estructura de decisión con if-elif-else
if num_1 > num_2:
    # Se ejecuta si num_1 es mayor que num_2
    print(f' El primer número ({num_1}) es MAYOR que el segundo ({num_2}).')
    print(f' Diferencia: {num_1 - num_2}')

elif num_1 < num_2:
    # Se ejecuta si num_1 es menor que num_2
    print(f' El segundo número ({num_2}) es MAYOR que el primero ({num_1}).')
    print(f' Diferencia: {num_2 - num_1}')

else:
    # Se ejecuta si num_1 == num_2 (ninguna de las condiciones anteriores fue verdadera)
    print(f' Los dos números son IGUALES ({num_1} = {num_2}).')

print("-" * 60)

"""
================================================================================
EJERCICIOS PROPUESTOS:
================================================================================

1. Modifica el programa para que también indique si los números son pares o impares.

2. Crea un programa que determine si un número es positivo, negativo o cero,
   y además indique si es par o impar.

3. Implementa un programa que determine si un año es bisiesto:
   - Es divisible por 4 Y
   - No es divisible por 100, EXCEPTO si también es divisible por 400
   Ejemplos: 2000 (bisiesto), 1900 (no bisiesto), 2024 (bisiesto)

4. Crea un programa que pida tres números y determine cuál es el mayor.

5. Implementa una calculadora simple que pida dos números y una operación
   (+, -, *, /) y muestre el resultado.

================================================================================
DIAGRAMA DE FLUJO:
================================================================================

    [Inicio]
       |
       v
  [Leer num_1]
       |
       v
  [Leer num_2]
       |
       v
  [num_1 > num_2?] --Sí--> [Mostrar "num_1 es mayor"]
       |                              |
       No                             |
       |                              |
       v                              |
  [num_1 < num_2?] --Sí--> [Mostrar "num_2 es mayor"]
       |                              |
       No                             |
       |                              |
       v                              |
  [Mostrar "Son iguales"] <-----------+
       |
       v
     [Fin]

================================================================================
ANÁLISIS:
================================================================================
Complejidad temporal: O(1) - Número constante de comparaciones
Complejidad espacial: O(1) - Solo almacenamos dos variables
================================================================================
"""
