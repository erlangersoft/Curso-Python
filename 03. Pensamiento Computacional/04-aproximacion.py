"""
================================================================================
04 - APROXIMACIÓN: Soluciones con Precisión Controlada
================================================================================

CONCEPTO:
---------
La aproximación es una técnica que permite encontrar soluciones "suficientemente
buenas" cuando:
- No existe una solución exacta (ej: √2, π)
- La solución exacta es difícil o costosa de calcular
- Una aproximación es suficiente para nuestros propósitos

EPSILON (ε):
------------
El valor epsilon define qué tan cerca queremos estar de la respuesta real.
Es el margen de error aceptable.

Ejemplos:
- epsilon = 0.1   → Precisión baja (1 decimal)
- epsilon = 0.01  → Precisión media (2 decimales)
- epsilon = 0.001 → Precisión alta (3 decimales)

TRADE-OFFS:
-----------
- Epsilon PEQUEÑO → Mayor precisión, MÁS iteraciones
- Epsilon GRANDE  → Menor precisión, MENOS iteraciones

EJEMPLO:
--------
Este programa calcula la raíz cuadrada de un número (incluso números
irracionales como √2) usando aproximación incremental.

================================================================================
"""

print("=" * 70)
print("CALCULADORA DE RAÍZ CUADRADA - MÉTODO DE APROXIMACIÓN")
print("=" * 70)

# Solicitar al usuario un número
objetivo = int(input('\nEscoge un número: '))

# Validar que el número sea positivo
if objetivo < 0:
    print("\nError: No se puede calcular la raíz cuadrada de un número negativo.")
else:
    # Configuración del algoritmo de aproximación
    epsilon = 0.01      # Precisión deseada (margen de error aceptable)
    paso = epsilon**2   # Tamaño del incremento (paso pequeño para mayor precisión)
    respuesta = 0.0     # Inicializar la respuesta en 0.0 (float)
    iteraciones = 0     # Contador de iteraciones
    
    print(f"\nParámetros:")
    print(f"  - Epsilon (precisión): {epsilon}")
    print(f"  - Paso (incremento): {paso}")
    print(f"\nBuscando la raíz cuadrada de {objetivo}...")
    print("-" * 70)
    
    # Incrementar la respuesta hasta que estemos suficientemente cerca
    # Condiciones:
    # 1. abs(respuesta² - objetivo) >= epsilon: Aún no estamos suficientemente cerca
    # 2. respuesta <= objetivo: No hemos pasado el límite superior
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
        iteraciones += 1
        
        # Mostrar progreso cada 10,000 iteraciones
        if iteraciones % 10000 == 0:
            print(f"Iteración {iteraciones}: respuesta = {respuesta:.4f}, "
                  f"respuesta² = {respuesta**2:.4f}, "
                  f"error = {abs(respuesta**2 - objetivo):.4f}")
    
    print("-" * 70)
    
    # Verificar si encontramos una aproximación válida
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'\nNo se encontró la raíz cuadrada de {objetivo}')
        print(f'El algoritmo superó el límite sin encontrar solución')
    else:
        print(f'\n¡Aproximación encontrada!')
        print(f'La raíz cuadrada de {objetivo} es aproximadamente {respuesta:.4f}')
        print(f'\nVerificación:')
        print(f'{respuesta:.4f}² = {respuesta**2:.6f}')
        print(f'Objetivo: {objetivo}')
        print(f'Error: {abs(respuesta**2 - objetivo):.6f} (< {epsilon})')
        print(f'\nEstadísticas:')
        print(f'Iteraciones realizadas: {iteraciones:,}')
        print(f'Precisión (epsilon): {epsilon}')

"""
================================================================================
ANÁLISIS DE COMPLEJIDAD:
================================================================================

Complejidad Temporal: O(√n / paso)
-----------------------------------
El número de iteraciones depende de:
- El valor de n (objetivo)
- El tamaño del paso (epsilon²)

Para n = 100, epsilon = 0.01:
- paso = 0.0001
- Iteraciones ≈ √100 / 0.0001 = 10 / 0.0001 = 100,000

Complejidad Espacial: O(1)
---------------------------
Solo usamos un número constante de variables.

================================================================================
EXPERIMENTO: EFECTO DEL EPSILON
================================================================================

Para objetivo = 2 (√2 ≈ 1.414):

Epsilon  | Paso      | Iteraciones | Resultado  | Error
---------|-----------|-------------|------------|--------
0.1      | 0.01      | ~141        | 1.41       | 0.004
0.01     | 0.0001    | ~14,140     | 1.4142     | 0.0002
0.001    | 0.000001  | ~1,414,000  | 1.41421    | 0.00001

Conclusión: Epsilon más pequeño = Mayor precisión pero MÁS tiempo

================================================================================
EJERCICIOS PROPUESTOS:
================================================================================

1. Modifica el programa para que el usuario pueda elegir el valor de epsilon
   y observe cómo afecta el número de iteraciones.

2. Implementa una función que calcule la raíz cúbica usando aproximación.

3. Crea un programa que aproxime el valor de π usando la serie de Leibniz:
   π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...

4. Implementa el método de Newton-Raphson para calcular raíces cuadradas
   (es mucho más eficiente que este método).

5. Modifica el programa para que muestre un gráfico del progreso de la
   aproximación (usando matplotlib).

================================================================================
COMPARACIÓN: APROXIMACIÓN vs ENUMERACIÓN
================================================================================

Característica       | Enumeración      | Aproximación
---------------------|------------------|------------------
Tipo de solución     | Solo enteros     | Números reales
Precisión            | Exacta           | Controlada (epsilon)
Números irracionales | No funciona      | Funciona bien
Eficiencia           | O(√n)            | O(√n / paso)
Complejidad código   | Simple           | Moderada

================================================================================
NOTA IMPORTANTE:
================================================================================
Este método es educativo pero NO es el más eficiente para calcular raíces
cuadradas. En la práctica, se usan métodos como:
- Búsqueda binaria (siguiente tema)
- Método de Newton-Raphson
- Funciones integradas: math.sqrt()

================================================================================
"""
