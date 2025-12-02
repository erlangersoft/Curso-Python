from abc import ABC, abstractmethod

class Figura(ABC):
    
    def __init__(self) -> None:
        pass
        
    @abstractmethod
    def calcularArea(self):
        pass
    
    @abstractmethod
    def calcularPerimetro(self):
        pass