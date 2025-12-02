"""
================================================================================
05 - BÚSQUEDA BINARIA: Algoritmo Divide y Vencerás
================================================================================

CONCEPTO:
---------
La búsqueda binaria es un algoritmo eficiente que divide el espacio de búsqueda
a la MITAD en cada iteración. Es similar a buscar una palabra en un diccionario:
abres por la mitad y decides si buscar en la primera o segunda mitad.

ESTRATEGIA "DIVIDE Y VENCERÁS":
--------------------------------
1. Define un rango con límite inferior (bajo) y superior (alto)
2. Calcula el punto medio del rango
3. Evalúa si el punto medio es la solución:
   - Si es muy bajo → Ajusta el límite inferior
   - Si es muy alto → Ajusta el límite superior
   - Si es correcto → ¡Encontrado!
4. Repite hasta encontrar la solución

VENTAJAS:
---------
Extremadamente eficiente: O(log n)
Reduce el espacio de búsqueda a la mitad en cada paso
Funciona con números reales (no solo enteros)

REQUISITOS:
-----------
El espacio de búsqueda debe estar ordenado o ser un rango continuo

EJEMPLO:
--------
Este programa calcula la raíz cuadrada de un número usando búsqueda binaria.
Es MUCHO más rápido que la enumeración exhaustiva o la aproximación.

================================================================================
"""

print("=" * 70)
print("CALCULADORA DE RAÍZ CUADRADA - BÚSQUEDA BINARIA")
print("=" * 70)

# Solicitar al usuario un número
objetivo = int(input('\nEscoge un número: '))

# Validar que el número sea positivo
if objetivo < 0:
    print("\nError: No se puede calcular la raíz cuadrada de un número negativo.")
else:
    # Configuración del algoritmo
    epsilon = 0.01              # Precisión deseada
    bajo = 0.0                  # Límite inferior del rango de búsqueda
    alto = max(1.0, objetivo)   # Límite superior (para n < 1, usar 1)
    respuesta = (alto + bajo) / 2  # Punto medio inicial
    iteraciones = 0             # Contador de iteraciones
    
    print(f"\nParámetros:")
    print(f"Epsilon (precisión): {epsilon}")
    print(f"Rango inicial: [{bajo}, {alto}]")
    print(f"\nBuscando la raíz cuadrada de {objetivo}...")
    print("-" * 70)
    
    # Iterar hasta que la aproximación sea suficientemente buena
    while abs(respuesta**2 - objetivo) >= epsilon:
        iteraciones += 1
        
        # Mostrar el progreso de cada iteración
        print(f"Iteración {iteraciones:2d}: "
              f"bajo={bajo:8.4f}, alto={alto:8.4f}, "
              f"respuesta={respuesta:8.4f}, "
              f"respuesta²={respuesta**2:8.4f}, "
              f"error={abs(respuesta**2 - objetivo):8.4f}")
        
        # Decidir en qué mitad buscar
        if respuesta**2 < objetivo:
            # La respuesta es muy baja, buscar en la mitad superior
            bajo = respuesta
        else:
            # La respuesta es muy alta, buscar en la mitad inferior
            alto = respuesta
        
        # Calcular el nuevo punto medio
        respuesta = (alto + bajo) / 2
        
        # Protección contra bucles infinitos (no debería ocurrir)
        if iteraciones > 1000:
            print("\nAdvertencia: Demasiadas iteraciones. Deteniendo...")
            break
    
    print("-" * 70)
    print(f'\nSolución encontrada!')
    print(f'La raíz cuadrada de {objetivo} es aproximadamente {respuesta:.6f}')
    print(f'\nVerificación:')
    print(f'{respuesta:.6f}² = {respuesta**2:.6f}')
    print(f'Objetivo: {objetivo}')
    print(f'Error: {abs(respuesta**2 - objetivo):.6f} (< {epsilon})')
    print(f'\nEstadísticas:')
    print(f'Iteraciones realizadas: {iteraciones}')
    print(f'Complejidad: O(log n) donde n = {objetivo}')
    
    # Comparación con otros métodos
    import math
    print(f'\nComparación con math.sqrt():')
    print(f'Nuestro resultado: {respuesta:.10f}')
    print(f'math.sqrt():       {math.sqrt(objetivo):.10f}')
    print(f'Diferencia:        {abs(respuesta - math.sqrt(objetivo)):.10f}')

"""
================================================================================
ANÁLISIS DE COMPLEJIDAD:
================================================================================

Complejidad Temporal: O(log n)
-------------------------------
El número de iteraciones crece logarítmicamente con el tamaño del problema.

Ejemplos de iteraciones necesarias:
- n = 10:         ~4 iteraciones
- n = 100:        ~7 iteraciones
- n = 1,000:      ~10 iteraciones
- n = 1,000,000:  ~20 iteraciones
- n = 1,000,000,000: ~30 iteraciones

Fórmula: iteraciones ≈ log₂(n / epsilon)

Complejidad Espacial: O(1)
---------------------------
Solo usamos un número constante de variables.

================================================================================
VISUALIZACIÓN DEL ALGORITMO:
================================================================================

Para objetivo = 25, epsilon = 0.01:

Iteración | Bajo   | Alto   | Medio  | Medio² | Acción
----------|--------|--------|--------|--------|------------------
1         | 0.00   | 25.00  | 12.50  | 156.25 | Muy alto → alto = 12.50
2         | 0.00   | 12.50  | 6.25   | 39.06  | Muy alto → alto = 6.25
3         | 0.00   | 6.25   | 3.13   | 9.77   | Muy bajo → bajo = 3.13
4         | 3.13   | 6.25   | 4.69   | 21.97  | Muy bajo → bajo = 4.69
5         | 4.69   | 6.25   | 5.47   | 29.88  | Muy alto → alto = 5.47
6         | 4.69   | 5.47   | 5.08   | 25.78  | Muy alto → alto = 5.08
7         | 4.69   | 5.08   | 4.88   | 23.84  | Muy bajo → bajo = 4.88
8         | 4.88   | 5.08   | 4.98   | 24.81  | Muy bajo → bajo = 4.98
9         | 4.98   | 5.08   | 5.03   | 25.29  | Muy alto → alto = 5.03
10        | 4.98   | 5.03   | 5.00   | 25.04  | Muy alto → alto = 5.00
11        | 4.98   | 5.00   | 4.99   | 24.92  | Error < 0.01

¡Solo 11 iteraciones para encontrar √25!

================================================================================
COMPARACIÓN CON OTROS MÉTODOS:
================================================================================

Para encontrar √1,000,000:

Método              | Complejidad | Iteraciones | Tiempo relativo
--------------------|-------------|-------------|----------------
Enumeración         | O(√n)       | ~1,000      | 1000x
Aproximación        | O(√n/paso)  | ~10,000,000 | 10,000,000x
Búsqueda Binaria    | O(log n)    | ~20         | 1x (más rápido)
Newton-Raphson      | O(log log n)| ~5          | 0.25x

Conclusión: La búsqueda binaria es DRAMÁTICAMENTE más eficiente.

================================================================================
EJERCICIOS PROPUESTOS:
================================================================================

1. Modifica el programa para calcular la raíz cúbica usando búsqueda binaria.

2. Implementa una búsqueda binaria para encontrar un elemento en una lista
   ordenada. Ejemplo: encontrar el número 42 en [1, 5, 12, 23, 42, 67, 89]

3. Crea un programa que use búsqueda binaria para encontrar el primer
   número malo en una secuencia (problema clásico de entrevistas).

4. Implementa un programa que encuentre el punto de rotación en un array
   rotado ordenado usando búsqueda binaria.

5. Modifica el programa para que calcule raíces n-ésimas (√ⁿx) donde el
   usuario puede elegir n.

================================================================================
APLICACIONES REALES:
================================================================================

La búsqueda binaria se usa en:
- Búsqueda en bases de datos indexadas
- Búsqueda en diccionarios y directorios telefónicos
- Algoritmos de juegos (ej: adivinar un número)
- Sistemas de archivos (búsqueda de bloques)
- Protocolos de red (búsqueda de rutas óptimas)
- Análisis de datos ordenados

================================================================================
NOTA IMPORTANTE:
================================================================================
La búsqueda binaria es uno de los algoritmos más importantes en ciencias de
la computación. Dominar este concepto es fundamental para:
- Entender algoritmos más avanzados
- Resolver problemas de optimización
- Pasar entrevistas técnicas
- Diseñar sistemas eficientes

¡Practica hasta que lo entiendas completamente!

================================================================================
"""
