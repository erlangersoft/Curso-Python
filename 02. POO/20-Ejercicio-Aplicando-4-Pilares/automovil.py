from vehiculo import Vehiculo

class Automovil(Vehiculo):
    """Clase Automóvil heredada de Vehículo. 
    """    
    def __init__(self, marca=None, modelo=None, anio=None, nroPuertas=None, nroPasajeros=None):
    
        super().__init__(marca, modelo, anio)
        
        if nroPuertas is not None:
            self._nroPuertas = nroPuertas
        else: # Asumiremos que un automóvil mínimamente puede tener 2 puertas.
            self._nroPuertas = 2
        
        if nroPasajeros is not None:
            self._nroPasajeros = nroPasajeros
        else: # Asumiremos que un automóvil mínimamente puede transportar 2 pasajeros.
            self._nroPasajeros = 2

    @property
    def nroPuertas(self):
        return self._nroPuertas

    @nroPuertas.setter
    def nroPuertas(self, value):
        self._nroPuertas = value

    @property
    def nroPasajeros(self):
        return self._nroPasajeros

    @nroPasajeros.setter
    def nroPasajeros(self, value):
        self._nroPasajeros = value

    def __str__(self) -> str:
        return f"""{super().__str__()}\nDatos Particulares del Automovil
    Nro. de Puertas:\t{self.nroPuertas}
    Nro. de Pasajeros:\t{self.nroPasajeros}
"""
    
    def conducir(self):
        print("Conduciendo Automovil.")