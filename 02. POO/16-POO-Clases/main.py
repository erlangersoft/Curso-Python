# Programación Orientada a Objetos:

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

# Fin definición de la clase

if __name__ == "__main__":
    # Crear un objeto de la clase Automovil:
    coche1 = Automovil()

    # Mostrar atributos del objeto accediendo directamente a sus propiedades:
    print("Datos de Coche 1 - Accediendo directamente")
    print(f"Marca: {coche1.marca}")
    print(f"Modelo: {coche1.modelo}")
    print(f"Año: {coche1.anio}")
    print(f"Cilindrada: {coche1.cilindrada}")
    print(f"Transmisión: {coche1.transmision}")
    print(f"Nro. de Pasajeros: {coche1.nroPasajeros}")
    print(f"Cap. de Carga: {coche1.capacidad_carga}")
    print(f"Color: {coche1.color}")
    print(f"Velocidad Inicial: {coche1.velocidad}")

    # Accediendo a sus métodos:
    coche1.acelerar()
    coche1.acelerar()
    coche1.acelerar()

    print(f"Velocidad Actual despues de acelerar 3 veces: {coche1.getVelocidad()}")

    coche1.frenar()
    coche1.frenar()
    print(f"Velocidad Actual despues de frenar 2 veces: {coche1.getVelocidad()}")


    # Crear un segundo objeto de la clase Automovil:
    coche2 = Automovil()

    # Mostrar atributos del objeto por medio de accesores y modificadores:
    print("Datos de Coche 2 - Usando Accesores y modificadores")

    coche2.setMarca("Nissan")
    coche2.setModelo("Muarano")
    coche2.setAnio(2020)
    coche2.setCilindrada(3000)
    coche2.setColor("Marrón")
    

    print(f"Marca: {coche2.getMarca()}")
    print(f"Modelo: {coche2.getModelo()}")
    print(f"Año: {coche2.getAnio()}")
    print(f"Cilindrada: {coche2.getCilindrada()}")
    print(f"Transmisión: {coche2.getTransmision()}")
    print(f"Nro. de Pasajeros: {coche2.getNroPasajeros()}")
    print(f"Cap. de Carga: {coche2.getCapacidad_carga()}")
    print(f"Color: {coche2.getColor()}")
    print(f"Velocidad Inicial: {coche2.getVelocidad()}")