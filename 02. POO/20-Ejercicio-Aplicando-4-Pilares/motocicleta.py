from vehiculo import Vehiculo

TIPOS_MOTORES = ["Motor de Combustión de Cuatro 4 tiempos", "Motor de Combustión Interna de 2 tiempos", "Monocilíndrico", "Bicilíndrico", "Tricilíndrico", "Tetracilindrico", "Hexacilíndrico", "Motor Eléctrico", "Motor Híbrido", "Motor Rotativo"]

class Motocicleta(Vehiculo):    
    
    def __init__(self, marca=None, modelo=None, anio=None, tipoMotor=None, cilindrada=None):
        super().__init__(marca, modelo, anio)
        
        if tipoMotor is not None:
            
            if tipoMotor not in TIPOS_MOTORES:
            
                self._tipoMotor = "Sin Especificar"
            else:
                self._tipoMotor = tipoMotor
        else:
            self._tipoMotor = "Sin Especificar"
            
        if cilindrada is not None:
            self._cilindrada = cilindrada
        else: # Por defecto asumiremos que tiene 150 cc.
            self._cilindrada = 150
            
    @property
    def tipoMotor(self):
        return self._tipoMotor

    @tipoMotor.setter
    def tipoMotor(self, value):
        
        if value not in TIPOS_MOTORES:
            self._tipoMotor = "Sin Especificar"
        else:        
            self._tipoMotor = value

    @property
    def cilindrada(self):
        return self._cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        self._cilindrada = value

    def conducir(self):
        print("Conduciendo Motocicleta.")
        
    def __str__(self) -> str:
        return f"""{super().__str__()}\nDatos Particulares de la Motocicleta
    Tipo de Motor:\t{self.tipoMotor}
    Cilindrada:\t\t{self.cilindrada} CC
"""