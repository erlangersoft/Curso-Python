# Definicion de variables:

cad1 = "Esto"
cad2 = "es"
cad3 = "Python"

# Mostrar variables con print:

print("Pasando las cadenas como parámetros al print.")
print(cad1, cad2, cad3)

# Concatenar una sola cadena:

cadena = cad1 + " " + cad2 + " " + cad3
print("Utilizando una variable")
print(cadena)

# También puede hacerse desde el print:
print("Formando la cadena en el print")
print(cad1 + " " + cad2 + " " + cad3)

# Tercera manera, utilizando f:
print("Utilizando formateo - interpolado")
print(f"{cad1} {cad2} {cad3}")

# Cuarta forma, con format:
print("Utilizando la cláusula format:")
print("Cadena 1: {}, Cadena 2: {}, Cadena 3: {}".format(cad1,cad2,cad3))

