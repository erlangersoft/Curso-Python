from figura import Figura

class Rectangulo(Figura):
    
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura
        
    def calcularArea(self):
        return self.base * self.altura
    
    def calcularPerimetro(self):
        return (self.base + self.altura) * 2