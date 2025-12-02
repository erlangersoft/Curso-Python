class FiguraGeometrica:
    def __init__(self, color, tamanio):
        self.color = color
        self.tamanio = tamanio

    def dibujar(self):
        print(f"Dibujando una figura geométrica de color {self.color} y tamaño {self.tamanio}")

class Circulo(FiguraGeometrica):
    def __init__(self, color, tamanio, radio):
        super().__init__(color, tamanio)
        self.radio = radio

    def dibujar(self):
        print(f"Dibujando un círculo de color {self.color}, tamaño {self.tamanio} y radio {self.radio}")

class Cuadrado(FiguraGeometrica):
    def __init__(self, color, tamanio, lado):
        super().__init__(color, tamanio)
        self.lado = lado

    def dibujar(self):
        print(f"Dibujando un cuadrado de color {self.color}, tamaño {self.tamanio} y lado {self.lado}")

class Triangulo(FiguraGeometrica):
    def __init__(self, color, tamanio, base, altura):
        super().__init__(color, tamanio)
        self.base = base
        self.altura = altura

    def dibujar(self):
        print(f"Dibujando un triángulo de color {self.color}, tamaño {self.tamanio}, base {self.base} y altura {self.altura}")

if __name__ == "__main__":
    # Crear objetos de las diferentes clases
    circulo = Circulo("rojo", 100, 50)
    cuadrado = Cuadrado("verde", 50, 10)
    triangulo = Triangulo("azul", 20, 10, 15)

    # Dibujar los objetos
    circulo.dibujar()
    cuadrado.dibujar()
    triangulo.dibujar()
