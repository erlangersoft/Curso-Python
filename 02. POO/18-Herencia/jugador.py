from persona import Persona

class Posiciones:
    LISTA_POSICIONES = ["Arquero", "Defensor", "Medio Campo", "Delantero"]

    def __init__(self, posicion):

        if posicion in self.LISTA_POSICIONES:
            self.posicion = posicion
        else:
            raise ValueError(f"La posición puede ser: {self.LISTA_POSICIONES}")


class Jugador(Persona):
    #posicion = Posiciones("")
    nroCamiseta = None
    nroGoles = None

    def __init__(self, nombre, aPaterno, aMaterno, fechaNacimiento, cedula, telefono, direccion, pos, nroCamiseta, nroGoles=0) -> None:
        super().__init__(nombre, aPaterno, aMaterno, fechaNacimiento, cedula, telefono, direccion)
        self.posicion = Posiciones(pos)
        self.nroCamiseta = nroCamiseta
        self.nroGoles = nroGoles
    
    def __str__(self):
        return f"""
{super().__str__()}

Ficha Técnica de Jugador:
=========================
Posición:\t\t{self.posicion.posicion}
Nro. de Camiseta:\t{self.nroCamiseta}
Nro. de Goles:\t\t{self.nroGoles}
                """