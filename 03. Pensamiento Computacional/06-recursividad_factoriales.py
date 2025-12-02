"""
================================================================================
06 - RECURSIVIDAD: Funciones que se Llaman a Sí Mismas
================================================================================

CONCEPTO:
---------
La recursividad es una técnica de programación donde una función se llama a
sí misma para resolver un problema dividiéndolo en subproblemas más pequeños.

Es como las muñecas rusas (matrioshkas): cada muñeca contiene una versión
más pequeña de sí misma, hasta llegar a la muñeca más pequeña.

COMPONENTES ESENCIALES:
-----------------------
Toda función recursiva DEBE tener:

1. CASO BASE: Condición que detiene la recursión
   - Sin caso base → Recursión infinita → Error de desbordamiento de pila
   
2. CASO RECURSIVO: Llamada a la función con un problema más pequeño
   - Debe acercarse al caso base en cada llamada

VENTAJAS:
---------
Código más elegante y fácil de leer
Natural para problemas que tienen estructura recursiva
Simplifica problemas complejos

DESVENTAJAS:
------------
Puede ser menos eficiente que soluciones iterativas
Consume más memoria (cada llamada usa espacio en la pila)
Python tiene límite de recursión (~1000 llamadas por defecto)

EJEMPLO:
--------
Calcular el factorial de un número usando recursividad.

Factorial de n (n!) = n × (n-1) × (n-2) × ... × 2 × 1
Ejemplos:
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 3! = 3 × 2 × 1 = 6
- 1! = 1
- 0! = 1 (por definición)

================================================================================
"""

def factorial(n):
    """
    Calcula el factorial de n de forma recursiva.
    
    El factorial de n (n!) es el producto de todos los enteros positivos
    desde 1 hasta n.
    
    Definición matemática:
    - factorial(0) = 1 (caso base)
    - factorial(1) = 1 (caso base)
    - factorial(n) = n × factorial(n-1) (caso recursivo)
    
    Args:
        n (int): Número entero no negativo (n >= 0)
    
    Returns:
        int: El factorial de n
    
    Raises:
        ValueError: Si n es negativo
        RecursionError: Si n es demasiado grande (> ~995)
    
    Ejemplos:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
        >>> factorial(1)
        1
    """
    # Validación: el factorial no está definido para números negativos
    if n < 0:
        raise ValueError(f"El factorial no está definido para números negativos (n = {n})")
    
    # CASO BASE: factorial de 0 y 1 es 1
    if n == 0 or n == 1:
        print(f"  {'  ' * (10 - n)}→ Caso base alcanzado: factorial({n}) = 1")
        return 1
    
    # CASO RECURSIVO: n! = n × (n-1)!
    print(f"  {'  ' * (10 - n)}→ Calculando: factorial({n}) = {n} × factorial({n-1})")
    resultado = n * factorial(n - 1)
    print(f"  {'  ' * (10 - n)}← Retornando: factorial({n}) = {resultado}")
    return resultado


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("CALCULADORA DE FACTORIAL - MÉTODO RECURSIVO")
    print("=" * 70)
    
    try:
        # Solicitar al usuario un número entero
        n = int(input('\nEscribe un entero no negativo: '))
        
        # Validar que el número no sea demasiado grande
        if n > 995:
            print(f"\nAdvertencia: {n} es demasiado grande.")
            print(f"   Python tiene un límite de recursión de ~1000 llamadas.")
            print(f"   Para números grandes, usa una solución iterativa.")
        else:
            print(f"\nCalculando factorial de {n}...")
            print("-" * 70)
            print("Traza de la recursión:")
            print("-" * 70)
            
            # Calcular el factorial
            resultado = factorial(n)
            
            print("-" * 70)
            print(f"\nResultado: {n}! = {resultado:,}")
            
            # Mostrar información adicional
            print(f"\nInformación:")
            print(f"Número de llamadas recursivas: {n}")
            print(f"Profundidad máxima de recursión: {n}")
            
    except ValueError as e:
        print(f"\nError: {e}")
    except RecursionError:
        print(f"\nError: Límite de recursión excedido.")
        print(f"El número es demasiado grande para calcular recursivamente.")

"""
================================================================================
VISUALIZACIÓN DE LA RECURSIÓN:
================================================================================

Para factorial(5):

LLAMADAS (bajando en la pila):
factorial(5) = 5 × factorial(4)
  factorial(4) = 4 × factorial(3)
    factorial(3) = 3 × factorial(2)
      factorial(2) = 2 × factorial(1)
        factorial(1) = 1  ← CASO BASE

RETORNOS (subiendo desde la pila):
        factorial(1) = 1
      factorial(2) = 2 × 1 = 2
    factorial(3) = 3 × 2 = 6
  factorial(4) = 4 × 6 = 24
factorial(5) = 5 × 24 = 120

================================================================================
PILA DE LLAMADAS (CALL STACK):
================================================================================

Paso 1: factorial(5) → Espera a factorial(4)
Paso 2: factorial(4) → Espera a factorial(3)
Paso 3: factorial(3) → Espera a factorial(2)
Paso 4: factorial(2) → Espera a factorial(1)
Paso 5: factorial(1) → Retorna 1 
Paso 6: factorial(2) → Retorna 2 × 1 = 2 
Paso 7: factorial(3) → Retorna 3 × 2 = 6 
Paso 8: factorial(4) → Retorna 4 × 6 = 24 
Paso 9: factorial(5) → Retorna 5 × 24 = 120 

Cada llamada ocupa espacio en memoria hasta que retorna.

================================================================================
ANÁLISIS DE COMPLEJIDAD:
================================================================================

Complejidad Temporal: O(n)
---------------------------
Se realizan n llamadas recursivas para calcular factorial(n).

Complejidad Espacial: O(n)
---------------------------
La pila de llamadas puede crecer hasta n niveles de profundidad.
Cada llamada ocupa espacio en memoria.

Comparación con versión iterativa:
- Recursiva: O(n) espacio
- Iterativa: O(1) espacio ← Más eficiente en memoria

================================================================================
VERSIÓN ITERATIVA (para comparación):
================================================================================

def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

Ventajas de la versión iterativa:
- Más eficiente en memoria: O(1) vs O(n)
- No tiene límite de recursión
- Generalmente más rápida

Ventajas de la versión recursiva:
- Más elegante y fácil de entender
- Refleja la definición matemática
- Natural para problemas recursivos

================================================================================
EJERCICIOS PROPUESTOS:
================================================================================

1. Implementa la secuencia de Fibonacci de forma recursiva:
   - F(0) = 0
   - F(1) = 1
   - F(n) = F(n-1) + F(n-2)
   
2. Crea una función recursiva que calcule la suma de los dígitos de un número.
   Ejemplo: suma_digitos(1234) = 1 + 2 + 3 + 4 = 10

3. Implementa una función recursiva que invierta una cadena de texto.
   Ejemplo: invertir("hola") = "aloh"

4. Crea una función recursiva que calcule el máximo común divisor (MCD)
   usando el algoritmo de Euclides.

5. Implementa las Torres de Hanoi de forma recursiva (problema clásico).

6. DESAFÍO: Implementa Fibonacci con memoización para hacerlo eficiente.

================================================================================
PROBLEMAS CLÁSICOS RECURSIVOS:
================================================================================

1. Torres de Hanoi
2. Secuencia de Fibonacci
3. Recorrido de árboles (preorden, inorden, postorden)
4. Búsqueda en directorios
5. Backtracking (Sudoku, N-Reinas)
6. Divide y vencerás (Merge Sort, Quick Sort)
7. Problemas de combinatoria (permutaciones, combinaciones)

================================================================================
LÍMITE DE RECURSIÓN EN PYTHON:
================================================================================

Python tiene un límite de recursión para prevenir desbordamiento de pila.

Ver el límite actual:
    import sys
    print(sys.getrecursionlimit())  # Por defecto: 1000

Cambiar el límite (¡usar con cuidado!):
    sys.setrecursionlimit(2000)

ADVERTENCIA: Aumentar el límite puede causar que Python se cuelgue si
la recursión es realmente infinita.

================================================================================
CUÁNDO USAR RECURSIVIDAD:
================================================================================

USA recursividad cuando:
- El problema tiene estructura naturalmente recursiva
- El código recursivo es más claro que el iterativo
- La profundidad de recursión es limitada y predecible
- Estás trabajando con estructuras de datos recursivas (árboles, grafos)

EVITA recursividad cuando:
- La eficiencia es crítica
- La profundidad puede ser muy grande
- Existe una solución iterativa simple
- Estás limitado en memoria

================================================================================
CONSEJO FINAL:
================================================================================

La recursividad es una herramienta poderosa, pero no siempre es la mejor
solución. Aprende a reconocer cuándo usarla y cuándo preferir iteración.

"Para entender la recursividad, primero debes entender la recursividad." 

================================================================================
"""
