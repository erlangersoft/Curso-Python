texto = "Ucatec Programación"
anio = 2023

# Se puede mostrar enviando parametros:
print(texto, anio)

# Pero para concatenar se debe convertir el tipo de dato:
print(texto + " " + str(anio))

# Otras conversiones de tipos:
numero = int(7)

print(numero)
print(type(numero))
print(type(str(numero)))

# Reasignando numero:
numero = float(7)

print(numero)
print(type(numero))
print(type(str(numero)))