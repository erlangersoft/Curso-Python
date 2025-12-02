# Curso Completo de Python

Este es un curso integral de Python organizado en 3 módulos progresivos que te llevarán desde los fundamentos básicos hasta conceptos avanzados de programación.

---

## Estructura del Curso

### Módulo 01: Sintaxis y Semántica de Python

**Objetivo**: Dominar los fundamentos del lenguaje Python

**Contenido** (29 archivos):
- Variables, tipos de datos y operadores
- Entrada/salida de datos
- Estructuras de control (condicionales, bucles)
- Funciones (definición, parámetros, recursividad)
- Listas y estructuras de datos básicas
- Manejo de archivos
- Material complementario en Jupyter Notebooks

**Archivos destacados**:
- `01-holamundo.py` - Primer programa en Python
- `10-condicionales.py` - Estructuras if/elif/else
- `13-bucle-for.py` y `14-bucle-while.py` - Iteraciones
- `15-funciones.py` - Definición y uso de funciones
- `18-crear-listas.py` - Manejo de listas

---

### Módulo 02: Programación Orientada a Objetos (POO)

**Objetivo**: Dominar el paradigma orientado a objetos en Python

**Contenido** (73 archivos):
- Clases y objetos
- Los 4 pilares de POO:
  - **Encapsulamiento**: Propiedades privadas y getters/setters
  - **Herencia**: Reutilización de código mediante jerarquías
  - **Polimorfismo**: Múltiples formas de un mismo método
  - **Abstracción**: Clases abstractas e interfaces
- Decomposición y abstracción
- Clases genéricas
- Manejo de excepciones
- Colecciones avanzadas

**Proyectos destacados**:
- `18-Herencia/` - Sistema de gestión deportiva (Persona → Jugador/Entrenador)
- `20-Ejercicio-Aplicando-4-Pilares/` - Sistema completo de registro de vehículos (371 líneas)
- `Clases Abstractas/` - Figuras geométricas con métodos abstractos
- `Encapsulamiento/` - Implementación de propiedades privadas

**Material teórico**:
- Notebooks Jupyter con teoría y ejemplos
- Diagramas de herencia
- Ejercicios prácticos

---

### Módulo 03: Pensamiento Computacional

**Objetivo**: Desarrollar habilidades para resolver problemas algorítmicos de manera eficiente

Bienvenido al módulo de **Pensamiento Computacional**. Este módulo te enseñará técnicas fundamentales para resolver problemas de manera eficiente usando algoritmos.

---

## Contenido del Módulo

Los archivos están ordenados numéricamente para seguir una progresión lógica de aprendizaje:

### 00. Introducción Teórica
- **`00-introduccion_pensamiento_computacional.ipynb`** - Notebook Jupyter con teoría completa, ejemplos interactivos y ejercicios propuestos

### 01. Fundamentos
- **`01-iteraciones.py`** - Control de flujo con bucles (`while`, `for`, `break`, `continue`)
- **`02-programas_ramificados.py`** - Toma de decisiones con estructuras condicionales

### 02. Técnicas Algorítmicas
- **`03-enumeracion_exhaustiva.py`** - Búsqueda por fuerza bruta (O(√n))
- **`04-aproximacion.py`** - Soluciones con precisión controlada usando epsilon
- **`05-busqueda_binaria.py`** - Algoritmo divide y vencerás (O(log n))

### 03. Conceptos Avanzados
- **`06-recursividad_factoriales.py`** - Funciones que se llaman a sí mismas
- **`07-testing_caja_negra.py`** - Validación de código con pruebas unitarias

---

## Objetivos de Aprendizaje

Al completar este módulo, serás capaz de:

1. Implementar y controlar bucles con `while` y `for`
2. Diseñar programas con lógica condicional compleja
3. Aplicar diferentes técnicas algorítmicas según el problema
4. Analizar la complejidad temporal de algoritmos
5. Implementar funciones recursivas correctamente
6. Escribir pruebas unitarias para validar código

---

## Comparación de Técnicas

| Técnica | Complejidad | Mejor para | Archivo |
|---------|-------------|------------|---------|
| Enumeración | O(√n) | Problemas pequeños, aprendizaje | `03-enumeracion_exhaustiva.py` |
| Aproximación | O(√n/paso) | Números irracionales | `04-aproximacion.py` |
| **Búsqueda Binaria** | O(log n) | Rangos grandes, máxima eficiencia | `05-busqueda_binaria.py` |
| **Recursividad** | Varía | Problemas naturalmente recursivos | `06-recursividad_factoriales.py` |

---

## Cómo Usar Este Módulo

### Opción 1: Aprendizaje Guiado (Recomendado)

1. **Lee primero el notebook**: `00-introduccion_pensamiento_computacional.ipynb`
   - Contiene toda la teoría y conceptos
   - Incluye ejemplos interactivos
   - Propone ejercicios para practicar

2. **Ejecuta los scripts en orden**: Del `01` al `07`
   - Cada archivo tiene comentarios educativos detallados
   - Incluye ejemplos de uso y casos de prueba
   - Propone ejercicios adicionales

3. **Experimenta y modifica**: 
   - Cambia valores y observa los resultados
   - Intenta resolver los ejercicios propuestos
   - Compara diferentes técnicas

### Opción 2: Referencia Rápida

Si ya conoces los conceptos, usa los archivos como referencia:
- Cada archivo es independiente y auto-contenido
- Los comentarios explican el código línea por línea
- Incluye análisis de complejidad y mejores prácticas

---

## Ejercicios Propuestos

Cada archivo incluye ejercicios al final. Aquí hay algunos desafíos adicionales:

### Nivel Básico
1. Modifica `01-iteraciones.py` para imprimir la tabla de multiplicar del 7
2. Usa `02-programas_ramificados.py` para determinar si un año es bisiesto
3. Encuentra todos los divisores de un número con `03-enumeracion_exhaustiva.py`

### Nivel Intermedio
4. Implementa el cálculo de raíz cúbica usando aproximación
5. Crea una búsqueda binaria para encontrar elementos en una lista ordenada
6. Implementa la secuencia de Fibonacci de forma recursiva

### Nivel Avanzado
7. Implementa las Torres de Hanoi recursivamente
8. Crea una función que calcule π usando la serie de Leibniz
9. Escribe tests completos para una calculadora con las 4 operaciones básicas

---

## Conceptos Clave

### Iteración
Ejecutar código repetidamente usando bucles.

### Ramificación
Tomar decisiones basadas en condiciones.

### Enumeración Exhaustiva
Probar todas las posibles soluciones (fuerza bruta).

### Aproximación
Encontrar soluciones "suficientemente buenas" con precisión controlada.

### Búsqueda Binaria
Dividir el espacio de búsqueda a la mitad en cada paso.

### Recursividad
Resolver problemas dividiéndolos en subproblemas más pequeños.

### Testing
Validar que el código funciona correctamente mediante pruebas.

---

## Recursos Adicionales

- [Python Documentation](https://docs.python.org/3/)
- [Big O Notation Cheat Sheet](https://www.bigocheatsheet.com/)
- [Unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [Python Tutor - Visualizador de Código](https://pythontutor.com/)

---

## Requisitos

- Python 3.6 o superior
- Jupyter Notebook (opcional, para el archivo `.ipynb`)
- Conocimientos básicos de Python (variables, funciones, operadores)

---

## Consejos de Estudio

1. **No te saltes el notebook**: La teoría es fundamental para entender el código
2. **Ejecuta el código**: No solo lo leas, ejecútalo y experimenta
3. **Haz los ejercicios**: La práctica es esencial para aprender
4. **Compara técnicas**: Entiende cuándo usar cada algoritmo
5. **Analiza la complejidad**: Aprende a evaluar la eficiencia del código

---

## Solución de Problemas

### Error: "No module named 'unittest'"
- `unittest` viene incluido con Python, no necesita instalación
- Verifica que estés usando Python 3.x

### Error: "RecursionError: maximum recursion depth exceeded"
- Estás usando un número demasiado grande para recursión
- Python tiene un límite de ~1000 llamadas recursivas
- Para números grandes, usa soluciones iterativas

### El programa es muy lento
- Revisa qué técnica estás usando
- La enumeración y aproximación pueden ser lentas para números grandes
- Considera usar búsqueda binaria para mejor rendimiento

---

## Notas Importantes

- Todos los archivos incluyen validación de entrada
- Los errores tipográficos del código original han sido corregidos
- Cada archivo es ejecutable de forma independiente
- Los comentarios están en español para facilitar el aprendizaje
- Se incluyen análisis de complejidad temporal y espacial

---

## Contribuciones

Este material es parte de un curso de Python. Si encuentras errores o tienes sugerencias de mejora, no dudes en compartirlas.

---

## Licencia

Material educativo de libre uso para aprendizaje de Python compartido por el profe Erlanger.

---

**¡Gracias por aprender conmigo!**

Y recuerda:

*"Para entender la recursividad, primero debes entender la recursividad."*
