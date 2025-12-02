from vehiculo import Vehiculo

class Camion(Vehiculo):
    
    def __init__(self, marca=None, modelo=None, anio=None, nroRuedas=None, torque=None, capCarga=None):
        super().__init__(marca, modelo, anio)
        
        if nroRuedas is not None and validarRuedas(nroRuedas):
            self._nroRuedas = nroRuedas
        else:
            self._nroRuedas = 0
            
        if torque is not None:
            self._torque = torque
        else:
            self._torque = 0
            
        if capCarga is not None:
            if validarCapacidad(capCarga):
                self._capCarga = capCarga
            else:
                self._capCarga = 0
        else:
            self._capCarga = 0
            
    @property
    def nroRuedas(self):
        return self._nroRuedas

    @nroRuedas.setter
    def nroRuedas(self, value):
        
        self._nroRuedas = value

    @property
    def torque(self):
        return self._torque

    @torque.setter
    def torque(self, value):
        self._torque = value

    @property
    def capCarga(self):
        return self._capCarga

    @capCarga.setter
    def capCarga(self, value):
        self._capCarga = value

    def conducir(self):
        print("Conduciendo Camión.")
    
    def __str__(self) -> str:
        cadena = f"""{super().__str__()}\nDatos Particulares del Camión
    Nro. Ruedas:\t{self.nroRuedas}
    Torque:\t\t{self.torque} Nm.
    Cap. de Carga:\t{self.capCarga} Kg."""

        if self.nroRuedas == 0 or self.torque == 0 or self.capCarga == 0:
            cadena += "\n\033[91m<<Debe completarse los datos del Vehículo.>>\033[0m"
        
        return cadena

# Funciones auxiliares:
# Validando que el número de ruedas sea minimamente 6:
def validarRuedas(valor):
    if valor >= 6:
        return True

    return False

# Validando que la capacidad de carga sólo pueda entar entre 1500 y 12000:
def validarCapacidad(valor):
    if 1500 <= valor <= 12000:
        return True
    
    return False