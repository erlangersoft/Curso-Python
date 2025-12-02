"""
Programa que genera la tabla de multiplicar de un número n sin usar ciclos repetitivos.
"""
def generar_tabla(num, resultados):
    if resultados > 1:
        generar_tabla(num, resultados-1)
    print(f"{num} * {resultados} = {num*resultados}")


n = int(input("Número: "))
m = int(input("Resultados: "))

generar_tabla(n, m)

#print(1 < n < 10)