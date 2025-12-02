from figura import Figura

class Cuadrado(Figura):
    def __init__(self, lado) -> None:
        self.lado = lado
    
    def calcularArea(self):
        return self.lado * self.lado
    
    def calcularPerimetro(self):
        return self.lado * 4