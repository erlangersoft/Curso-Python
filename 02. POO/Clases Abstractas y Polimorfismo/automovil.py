class  Vehiculo():
    
    def __init__(self):
        pass

    def desplazamiento(self):
        pass

    def mostrar(self):
        print(f"Tipo:\t{self.__class__.__name__}")


class Automovil(Vehiculo):
    def desplazamiento(self): 
        print("Se desplaza utilizando cuatro ruedas.")

class Motocicleta(Vehiculo):
    def desplazamiento(self):
        print("Se desplaza utilizando dos ruedas.")

class Camion(Vehiculo):
    def desplazamiento(self):
        print("Se desplaza utilizando seis ruedas.")

# main:
vehiculo1 = Automovil()
#vehiculo1.desplazamiento()

vehiculo2 = Motocicleta()
#vehiculo2.desplazamiento()

vehiculo3 = Camion()
#vehiculo3.desplazamiento()

def mostrar_datos(vehiculo):
    print(f"Tipo:\t{type(vehiculo).__name__}")
    vehiculo.desplazamiento()

mostrar_datos(vehiculo1)
mostrar_datos(vehiculo2)
mostrar_datos(vehiculo3)

vehiculo1.mostrar()
vehiculo2.mostrar()
vehiculo3.mostrar()
