class Deporte:
    nombre = None
    creacion = None
    record = None

    def __init__(self,nombre,creacion,record=0):
        self.nombre = nombre
        self.creacion = creacion
        self.record = record

################################################################    
class Destreza(Deporte):
    herramienta = None
    marcaHerramienta = None

    def __init__(self,nombre,creacion,herramienta,marcaHerramienta):
        super().__init__(nombre,creacion)
        self.herramienta = herramienta
        self.marcaHerramienta = marcaHerramienta

################################################################
class Estrategia(Deporte):
    nroParticipantes = None
    gradoConocimiento = None

    def __init__(self,nombre,creacion,nroParticipantes,gradoConocimiento):
        super().__init__(nombre,creacion)
        self.nroParticipantes = nroParticipantes
        self.gradoConocimiento = gradoConocimiento


################################################################
class Resistencia(Deporte):
    recorrido = None
    nroParticipantesEquipo = None

    def __init__(self,nombre,creacion,recorrido,nroParticipantesEquipo):
        super().__init__(nombre,creacion)
        self.recorrido = recorrido
        self.nroParticipantesEquipo = nroParticipantesEquipo
