from abc import ABC, abstractmethod

class Vehiculo(ABC):
    
    def __init__(self, marca=None, modelo=None, anio=None) -> None: 
        # Colocar -> None: al final de su constructor de clase en Python, está indicando que el constructor no devolverá ningún valor. Esto es equivalente a escribir pass en el cuerpo del constructor.
        
        if marca is None:
            self._marca = "Sin Marca"
        else:
            self._marca = marca
        
        if modelo is None:
            self._modelo = "Sin Modelo"
        else:
            self._modelo = modelo
        
        if anio is None:
            self._anio = 0
        else:
            self._anio = anio

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, value):
        self._anio = value


    @abstractmethod
    def conducir(self):
        pass

    def __str__(self) -> str:
        return f"""Información General del Vehículo
    Marca:\t{self.marca}
    Modelo:\t{self.modelo}
    Año:\t{self.anio}
    """
