class Equipo:
    nombreClub = None
    nroJugadores = None

    def __init__(self, nombreClub, nroJugadores=0):
        self.nombreClub = nombreClub
        self.nroJugadores = nroJugadores
    
    def getNombreClub(self):
        return self.nombreClub

    def __str__(self):
        return f"""
Nombre del Club:\t{self.nombreClub}
Jugadores Registrados:\t{self.nroJugadores}
"""