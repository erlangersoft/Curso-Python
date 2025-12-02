from figura import Figura
from cuadrado import Cuadrado
from rectangulo import Rectangulo

lado = int(input("Ingresar lado: "))
fig1 = Cuadrado(lado)

print(f"\tÁrea: {fig1.calcularArea()}")
print(f"\tPerímetro: {fig1.calcularPerimetro()}")

base = int(input("Ingresar base: "))
altura = int(input("Ingresar altura: "))
fig2 = Rectangulo(base, altura)

print(f"\tÁrea: {fig1.calcularArea()}")
print(f"\tPerímetro: {fig1.calcularPerimetro()}")

