import math

def calcular_area(lado1, lado2, lado3):
    # Usamos la fórmula de Herón para calcular el área de un triángulo
    s = (lado1 + lado2 + lado3) / 2
    area = math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))
    return area

def calcular_perimetro(lado1, lado2, lado3):
    perimetro = lado1 + lado2 + lado3
    return perimetro

def main():
    try:
        lado1 = float(input("Lado 1: "))
        lado2 = float(input("Lado 2: "))
        lado3 = float(input("Lado 3: "))
        
        area = calcular_area(lado1, lado2, lado3)
        perimetro = calcular_perimetro(lado1, lado2, lado3)
        
        print(f"Área: {area:.2f}")
        print(f"Perímetro: {perimetro:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()