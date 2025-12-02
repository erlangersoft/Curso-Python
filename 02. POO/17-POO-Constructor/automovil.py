# Definir una clase (molde para crear objetos de ese tipo)
# (Coche) con caracteristicas similares.

class Automovil:

    # Atributos de la clase Automovil:
    marca = "Toyota"
    modelo = "Hilux"
    anio = 2023
    cilindrada = 2700
    transmision = "mecanica"
    nroPasajeros = 5
    capacidad_carga = 1000
    color = "Rojo"
    velocidad = 0

    # Constructor de la clase Automovil:
    def __init__(self, marca, modelo, anio, cilindrada, trans, nroPasajeros, capacidad, color, velocidad):
        """_summary_

        Args:
            marca (_str_): _description_
            modelo (_str_): _description_
            anio (_int_): _description_
            cilindrada (_int_): _description_
            trans (_str_): _description_
            nroPasajeros (_int_): _description_
            capacidad (_int_): _description_
            color (_str_): _description_
            velocidad (_int_): _description_
        """        
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.cilindrada = cilindrada
        self.transmision = trans
        self.nroPasajeros = nroPasajeros
        self.capacidad_carga = capacidad
        self.color = color
        self.velocidad = velocidad


    # metodos de la clase:
    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        self.velocidad -= 10
    
    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca
    
    def getModelo(self):
        return self.modelo
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getAnio(self):
        return self.anio
    
    def setAnio(self, anio):
        self.anio = anio
    
    def getCilindrada(self):
        return self.cilindrada
    
    def setCilindrada(self, cilindrada):
        self.cilindrada = cilindrada
    
    def getTransmision(self):
        return self.transmision
    
    def setTransmision(self, transmision):
        self.transmision = transmision
    
    def getNroPasajeros(self):
        return self.nroPasajeros
    
    def setNroPasajeros(self, nroPasajeros):
        self.nroPasajeros = nroPasajeros
    
    def getCapacidad_carga(self):
        return self.capacidad_carga
    
    def setCapacidad_carga(self, capacidad_carga):
        self.capacidad_carga = capacidad_carga
    
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

    def getVelocidad(self):
        return self.velocidad
    
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad

    def __str__(self):
        
        cadena = f"\nMarca: {self.marca}"
        cadena += f"\nModelo: {self.modelo}"
        cadena += f"\nAño: {self.anio}"
        cadena += f"\nCilindrada: {self.cilindrada}"
        cadena += f"\nTransmisión: {self.transmision}"
        cadena += f"\nNro. de Pasajeros: {self.nroPasajeros}"
        cadena += f"\nCap. de Carga: {self.capacidad_carga}"
        cadena += f"\nColor: {self.color}"
        cadena += f"\nVelocidad Inicial: {self.velocidad}"

        return cadena

# Fin definición de la clase