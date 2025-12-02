# Programa que genera la tabla de multiplicar de 1 a M de un número N.

n = int(input("Ingresar n: "))
m = int(input("Ingresar m: "))

i = 0

while True:
    i+=1
    print(f"{n} * {i} = {n*i}")
    
    if i == m: break
