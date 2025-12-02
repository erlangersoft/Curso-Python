# Imprime 10 primeros números decimales, sabiendo que se inicia en cero.
print("Imprime los 10 primeros números decimales")
for i in range(0, 10):
    print(f"{i}\t", end="")


print("\nPrograma que lee varios nuemros separados por espacio y los muestra")
cad = input()
numeros = [int(num) for num in cad.split()]

print(numeros)