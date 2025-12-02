"""
================================================================================
07 - TESTING DE CAJA NEGRA: Validación de Código
================================================================================

CONCEPTO:
---------
El testing (pruebas) es el proceso de verificar que nuestro código funciona
correctamente. Es una parte FUNDAMENTAL del desarrollo de software profesional.

TESTING DE CAJA NEGRA:
-----------------------
En el testing de "caja negra", probamos una función sin conocer su
implementación interna. Solo nos importa:

📥 ENTRADA: Qué datos le damos a la función
📤 SALIDA: Qué resultado esperamos recibir

No nos importa CÓMO funciona internamente, solo que produzca el resultado
correcto para cada entrada.

POR QUÉ ES IMPORTANTE:
----------------------
✅ Detecta errores antes de que lleguen a producción
✅ Documenta cómo debe comportarse el código
✅ Facilita refactorización (cambiar código sin romper funcionalidad)
✅ Aumenta la confianza en el código
✅ Es requerido en desarrollo profesional

TIPOS DE TESTS:
---------------
1. 🎯 Casos normales: Entradas típicas esperadas
2. 🔍 Casos límite: Valores en los bordes (0, 1, -1, máximo, mínimo)
3. ⚠️  Casos de error: Entradas inválidas que deben manejarse
4. 🎲 Casos especiales: Situaciones particulares del dominio

FRAMEWORK: unittest
-------------------
Python incluye el módulo 'unittest' para crear y ejecutar pruebas unitarias.

================================================================================
"""

import unittest

# ============================================================================
# FUNCIONES A PROBAR
# ============================================================================

def suma(num_1, num_2):
    """
    Suma dos números.
    
    Args:
        num_1: Primer número (int o float)
        num_2: Segundo número (int o float)
    
    Returns:
        La suma de num_1 y num_2
    
    Ejemplos:
        >>> suma(10, 5)
        15
        >>> suma(-3, 7)
        4
    """
    return num_1 + num_2


def resta(num_1, num_2):
    """
    Resta dos números.
    
    Args:
        num_1: Primer número (int o float)
        num_2: Segundo número (int o float)
    
    Returns:
        La resta de num_1 - num_2
    """
    return num_1 - num_2


def multiplicacion(num_1, num_2):
    """
    Multiplica dos números.
    
    Args:
        num_1: Primer número (int o float)
        num_2: Segundo número (int o float)
    
    Returns:
        El producto de num_1 × num_2
    """
    return num_1 * num_2


def division(num_1, num_2):
    """
    Divide dos números.
    
    Args:
        num_1: Dividendo (int o float)
        num_2: Divisor (int o float, debe ser diferente de 0)
    
    Returns:
        El cociente de num_1 / num_2
    
    Raises:
        ValueError: Si num_2 es 0 (división por cero)
    """
    if num_2 == 0:
        raise ValueError("No se puede dividir por cero")
    return num_1 / num_2


# ============================================================================
# CLASE DE PRUEBAS (TEST CASE)
# ============================================================================

class CajaNegraTest(unittest.TestCase):
    """
    Clase que contiene todas las pruebas para las funciones matemáticas.
    
    Cada método que comienza con 'test_' es una prueba individual.
    unittest ejecutará automáticamente todos estos métodos.
    """
    
    # ========================================================================
    # TESTS PARA LA FUNCIÓN SUMA
    # ========================================================================
    
    def test_suma_dos_positivos(self):
        """Prueba suma de dos números positivos"""
        num_1 = 10
        num_2 = 5
        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, 15, "10 + 5 debe ser 15")
    
    def test_suma_dos_negativos(self):
        """Prueba suma de dos números negativos"""
        num_1 = -10
        num_2 = -5
        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, -15, "-10 + (-5) debe ser -15")
    
    def test_suma_positivo_negativo(self):
        """Prueba suma de un número positivo y uno negativo"""
        num_1 = 10
        num_2 = -3
        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, 7, "10 + (-3) debe ser 7")
    
    def test_suma_con_cero(self):
        """Prueba suma con cero (elemento neutro)"""
        num_1 = 10
        num_2 = 0
        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, 10, "10 + 0 debe ser 10")
    
    def test_suma_decimales(self):
        """Prueba suma de números decimales"""
        num_1 = 3.5
        num_2 = 2.7
        resultado = suma(num_1, num_2)
        self.assertAlmostEqual(resultado, 6.2, places=1, 
                              msg="3.5 + 2.7 debe ser aproximadamente 6.2")
    
    # ========================================================================
    # TESTS PARA LA FUNCIÓN RESTA
    # ========================================================================
    
    def test_resta_positivos(self):
        """Prueba resta de números positivos"""
        resultado = resta(10, 3)
        self.assertEqual(resultado, 7, "10 - 3 debe ser 7")
    
    def test_resta_negativos(self):
        """Prueba resta de números negativos"""
        resultado = resta(-5, -3)
        self.assertEqual(resultado, -2, "-5 - (-3) debe ser -2")
    
    def test_resta_con_cero(self):
        """Prueba resta con cero"""
        resultado = resta(10, 0)
        self.assertEqual(resultado, 10, "10 - 0 debe ser 10")
    
    # ========================================================================
    # TESTS PARA LA FUNCIÓN MULTIPLICACIÓN
    # ========================================================================
    
    def test_multiplicacion_positivos(self):
        """Prueba multiplicación de números positivos"""
        resultado = multiplicacion(4, 5)
        self.assertEqual(resultado, 20, "4 × 5 debe ser 20")
    
    def test_multiplicacion_por_cero(self):
        """Prueba multiplicación por cero"""
        resultado = multiplicacion(10, 0)
        self.assertEqual(resultado, 0, "10 × 0 debe ser 0")
    
    def test_multiplicacion_por_uno(self):
        """Prueba multiplicación por uno (elemento neutro)"""
        resultado = multiplicacion(7, 1)
        self.assertEqual(resultado, 7, "7 × 1 debe ser 7")
    
    def test_multiplicacion_negativos(self):
        """Prueba multiplicación de números negativos"""
        resultado = multiplicacion(-3, -4)
        self.assertEqual(resultado, 12, "(-3) × (-4) debe ser 12")
    
    # ========================================================================
    # TESTS PARA LA FUNCIÓN DIVISIÓN
    # ========================================================================
    
    def test_division_normal(self):
        """Prueba división normal"""
        resultado = division(10, 2)
        self.assertEqual(resultado, 5, "10 / 2 debe ser 5")
    
    def test_division_con_decimales(self):
        """Prueba división que resulta en decimal"""
        resultado = division(7, 2)
        self.assertAlmostEqual(resultado, 3.5, places=1,
                              msg="7 / 2 debe ser 3.5")
    
    def test_division_por_cero(self):
        """Prueba que dividir por cero lance una excepción"""
        with self.assertRaises(ValueError, msg="Dividir por cero debe lanzar ValueError"):
            division(10, 0)
    
    def test_division_de_cero(self):
        """Prueba división de cero"""
        resultado = division(0, 5)
        self.assertEqual(resultado, 0, "0 / 5 debe ser 0")
    
    def test_division_negativos(self):
        """Prueba división de números negativos"""
        resultado = division(-10, 2)
        self.assertEqual(resultado, -5, "-10 / 2 debe ser -5")


# ============================================================================
# EJECUCIÓN DE LAS PRUEBAS
# ============================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("EJECUTANDO PRUEBAS UNITARIAS - TESTING DE CAJA NEGRA")
    print("=" * 70)
    print()
    
    # Ejecutar todas las pruebas
    # verbosity=2 muestra información detallada de cada prueba
    unittest.main(verbosity=2)

"""
================================================================================
MÉTODOS DE ASSERTION MÁS COMUNES:
================================================================================

assertEqual(a, b)           → Verifica que a == b
assertNotEqual(a, b)        → Verifica que a != b
assertTrue(x)               → Verifica que x es True
assertFalse(x)              → Verifica que x es False
assertIs(a, b)              → Verifica que a is b (mismo objeto)
assertIsNone(x)             → Verifica que x is None
assertIn(a, b)              → Verifica que a está en b
assertIsInstance(a, type)   → Verifica que a es instancia de type
assertRaises(Exception)     → Verifica que se lance una excepción
assertAlmostEqual(a, b)     → Verifica que a ≈ b (para floats)
assertGreater(a, b)         → Verifica que a > b
assertLess(a, b)            → Verifica que a < b

================================================================================
ESTRUCTURA DE UN TEST:
================================================================================

1. ARRANGE (Preparar): Configurar los datos de prueba
   num_1 = 10
   num_2 = 5

2. ACT (Actuar): Ejecutar la función a probar
   resultado = suma(num_1, num_2)

3. ASSERT (Afirmar): Verificar el resultado
   self.assertEqual(resultado, 15)

Este patrón se conoce como "AAA" (Arrange, Act, Assert)

================================================================================
EJECUTAR LAS PRUEBAS:
================================================================================

Desde la línea de comandos:

1. Ejecutar este archivo:
   python 07-testing_caja_negra.py

2. Ejecutar con más detalle:
   python 07-testing_caja_negra.py -v

3. Ejecutar solo un test específico:
   python -m unittest 07-testing_caja_negra.CajaNegraTest.test_suma_dos_positivos

================================================================================
INTERPRETANDO LOS RESULTADOS:
================================================================================

. (punto)  → Test pasó correctamente ✅
F (F)      → Test falló (Failure) ❌
E (E)      → Test tuvo un error (Error) ⚠️

Ejemplo de salida:
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK

Esto significa que los 10 tests pasaron correctamente.

================================================================================
EJERCICIOS PROPUESTOS:
================================================================================

1. Añade una función potencia(base, exponente) y crea tests para ella.
   Casos a probar:
   - Exponente positivo
   - Exponente cero (cualquier número^0 = 1)
   - Exponente negativo
   - Base cero

2. Crea una función es_primo(n) y escribe tests exhaustivos:
   - Números primos (2, 3, 5, 7, 11, etc.)
   - Números no primos (4, 6, 8, 9, etc.)
   - Casos especiales (0, 1, números negativos)

3. Implementa una función factorial(n) y crea tests que verifiquen:
   - factorial(0) = 1
   - factorial(1) = 1
   - factorial(5) = 120
   - Que lance error con números negativos

4. Crea una función invertir_cadena(texto) y prueba:
   - Cadenas normales
   - Cadena vacía
   - Cadenas con espacios
   - Palíndromos

5. DESAFÍO: Implementa TDD (Test-Driven Development):
   - Primero escribe los tests
   - Luego implementa la función para que pase los tests

================================================================================
BUENAS PRÁCTICAS DE TESTING:
================================================================================

✅ DO (Hacer):
   - Escribe tests para cada función importante
   - Prueba casos normales, límite y de error
   - Usa nombres descriptivos para los tests
   - Mantén los tests simples y enfocados
   - Ejecuta los tests frecuentemente

❌ DON'T (No hacer):
   - No pruebes código trivial (getters/setters simples)
   - No hagas tests que dependan de otros tests
   - No ignores tests que fallan
   - No escribas tests sin assertions
   - No pruebes implementación, prueba comportamiento

================================================================================
COBERTURA DE CÓDIGO (CODE COVERAGE):
================================================================================

La cobertura indica qué porcentaje de tu código está siendo probado.

Instalar coverage:
    pip install coverage

Ejecutar con coverage:
    coverage run -m unittest 07-testing_caja_negra.py
    coverage report
    coverage html  # Genera reporte HTML

Meta recomendada: > 80% de cobertura

================================================================================
TESTING EN EL MUNDO REAL:
================================================================================

En proyectos profesionales:
- 🏢 Empresas requieren tests antes de aceptar código
- 🔄 CI/CD ejecuta tests automáticamente en cada commit
- 📊 Se mide y reporta la cobertura de código
- 🐛 Los bugs se reproducen primero con un test
- 📝 Los tests sirven como documentación viva

Frameworks populares:
- unittest (incluido en Python)
- pytest (más moderno y popular)
- nose2
- doctest

================================================================================
PIRÁMIDE DE TESTING:
================================================================================

                    /\\
                   /  \\  E2E Tests (pocos, lentos)
                  /____\\
                 /      \\
                / Integr \\  Integration Tests (algunos, medianos)
               /__________\\
              /            \\
             /   Unit Tests \\  Unit Tests (muchos, rápidos)
            /________________\\

La base debe ser sólida con muchos tests unitarios.

================================================================================
CONSEJO FINAL:
================================================================================

"El código sin tests es código legacy desde el día 1."
- Michael Feathers

Desarrolla el hábito de escribir tests. Te ahorrará HORAS de debugging
y te dará confianza para refactorizar y mejorar tu código.

¡Los buenos desarrolladores escriben tests! 🧪✅

================================================================================
"""
