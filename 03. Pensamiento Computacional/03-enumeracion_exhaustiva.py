"""
================================================================================
03 - ENUMERACIÓN EXHAUSTIVA: Búsqueda por Fuerza Bruta
================================================================================

CONCEPTO:
---------
La enumeración exhaustiva (también llamada "fuerza bruta") es una técnica
que consiste en probar TODAS las posibles soluciones hasta encontrar la correcta.

CARACTERÍSTICAS:
----------------
Ventajas:
   - Simple de implementar
   - Garantiza encontrar la solución si existe
   - No requiere conocimientos matemáticos avanzados

Desventajas:
   - Puede ser muy lento para problemas grandes
   - Ineficiente en términos de tiempo de ejecución

CUÁNDO USAR:
------------
- Problemas pequeños donde la eficiencia no es crítica
- Cuando no conocemos un algoritmo más eficiente
- Para validar resultados de algoritmos más complejos

EJEMPLO:
--------
Este programa encuentra la raíz cuadrada ENTERA de un número usando
enumeración exhaustiva: prueba todos los números desde 0 hasta encontrar
uno cuyo cuadrado sea igual al objetivo.

================================================================================
"""

print("=" * 70)
print("CALCULADORA DE RAÍZ CUADRADA ENTERA - ENUMERACIÓN EXHAUSTIVA")
print("=" * 70)

# Solicitar al usuario un número entero
objetivo = int(input('\nEscoge un número entero positivo: '))

# Validar que el número sea positivo
if objetivo < 0:
    print("\nError: No se puede calcular la raíz cuadrada de un número negativo.")
else:
    # Inicializar la respuesta en 0
    respuesta = 0
    iteraciones = 0  # Contador para ver cuántas iteraciones necesitamos
    
    print(f"\nBuscando la raíz cuadrada de {objetivo}...")
    print("-" * 70)
    
    # Probar todos los números desde 0 hasta que el cuadrado supere el objetivo
    while respuesta**2 < objetivo:
        iteraciones += 1
        respuesta += 1
        
        # Mostrar progreso cada 100 iteraciones (solo para números grandes)
        if iteraciones % 100 == 0:
            print(f"Probando... {respuesta}² = {respuesta**2}")
    
    print("-" * 70)
    
    # Verificar si encontramos una raíz cuadrada exacta
    if respuesta**2 == objetivo:
        print(f'\n¡Encontrado! La raíz cuadrada de {objetivo} es {respuesta}')
        print(f'Verificación: {respuesta}² = {respuesta**2}')
    else:
        print(f'\n{objetivo} no tiene una raíz cuadrada exacta.')
        print(f'El valor más cercano es {respuesta - 1}')
        print(f'Verificación: {respuesta - 1}² = {(respuesta - 1)**2}')
        print(f'                 {respuesta}² = {respuesta**2}')
    
    print(f'\nEstadísticas:')
    print(f'Iteraciones realizadas: {iteraciones}')
    print(f'Complejidad: O(√n) donde n = {objetivo}')

"""
================================================================================
ANÁLISIS DE COMPLEJIDAD:
================================================================================

Complejidad Temporal: O(√n)
---------------------------
Para encontrar la raíz cuadrada de n, necesitamos aproximadamente √n iteraciones.

Ejemplos:
- Para n = 100:   ~10 iteraciones
- Para n = 10,000: ~100 iteraciones
- Para n = 1,000,000: ~1,000 iteraciones

Complejidad Espacial: O(1)
---------------------------
Solo usamos un número constante de variables (objetivo, respuesta, iteraciones).

================================================================================
COMPARACIÓN CON OTROS MÉTODOS:
================================================================================

Método              | Complejidad | Iteraciones para n=1,000,000
--------------------|-------------|------------------------------
Enumeración         | O(√n)       | ~1,000
Búsqueda Binaria    | O(log n)    | ~20
Método de Newton    | O(log log n)| ~5

================================================================================
EJERCICIOS PROPUESTOS:
================================================================================

1. Modifica el programa para que encuentre todos los divisores de un número.
   Ejemplo: divisores de 12 = [1, 2, 3, 4, 6, 12]

2. Implementa un programa que determine si un número es primo usando
   enumeración exhaustiva.

3. Crea un programa que encuentre el máximo común divisor (MCD) de dos
   números usando el algoritmo de Euclides.

4. Implementa un programa que genere todos los números primos menores
   que un número dado (Criba de Eratóstenes).

5. Modifica el programa para que también calcule la raíz cúbica entera.

================================================================================
VISUALIZACIÓN DEL ALGORITMO:
================================================================================

Para objetivo = 25:

Iteración 1: 0² = 0   < 25  Continuar
Iteración 2: 1² = 1   < 25  Continuar
Iteración 3: 2² = 4   < 25  Continuar
Iteración 4: 3² = 9   < 25  Continuar
Iteración 5: 4² = 16  < 25  Continuar
Iteración 6: 5² = 25  = 25  ¡Encontrado!

================================================================================
"""
