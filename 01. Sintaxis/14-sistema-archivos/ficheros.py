from io import open
import pathlib

#Utilizando el path absoluto:

ruta = str(pathlib.Path().absolute()) + "\\Sintaxis\\14-sistema-archivos\\fichero.txt"
print("url: " + ruta)

# Abrir archivo:
#archivo = open("./Sintaxis/14-sistema-archivos/fichero.txt", "a+")
#archivo = open("fichero.txt", "a+")
archivo = open(ruta, "a+")

# Escribir en el archivo:
archivo.write("***********Soy un texto generado desde Python***********\n")
# Cerrar el archivo:
archivo.close()

# Accediendo al fichero para leer el contenido:
archivo_lectura = open(ruta, "r")

#contenido = archivo_lectura.read()
#print(contenido)

#print("Desde un ciclo linea a línea:")
#for linea in archivo_lectura:
#    print(linea, end="")

lineas = archivo_lectura.readlines()
archivo_lectura.close()

num = len(lineas)
#print(lineas)
for i in range(num):
    print(lineas[i], end="")