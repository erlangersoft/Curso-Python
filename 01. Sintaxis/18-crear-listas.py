"""
Son colecciones de datos o valores. Similar a lo que ocurre en otroslenguajes con arrays. Se construyen bajo un unico nombre, para acceder a los valores debemos usar un indice num{erico.
"""
n = int(input("Ingresar Número de Elementos: "))

numeros = []
for i in range(0, n):
    num = int(input(f"Elemento[{i}]: "))
    numeros.append(num)

print("Elementos de la lista:")
for i in range(0, n):
    print(f"Elemento[{i}]: {numeros[i]}")
