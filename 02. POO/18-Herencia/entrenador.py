from persona import Persona

class Entrenador(Persona):
    aniosExperiencia = None
    clubes = []

    def __init__(self, nombre, aPaterno, aMaterno, fechaNacimiento, cedula, telefono, direccion, aniosExperiencia):
        super().__init__(nombre, aPaterno, aMaterno, fechaNacimiento, cedula, telefono, direccion)
        self.aniosExperiencia = aniosExperiencia
    
    @classmethod
    def agregar_club(cls, club):
        cls.clubes.append(club)
    
    @classmethod
    def borrar_club(cls, club):
        cls.clubes.remove(club)

    def __str__(self):
        aux = len(self.clubes) - 1

        cadena="["
        for club in self.clubes:
            cadena += club.getNombreClub()
            
            if aux > 0:
                cadena += ", "
            aux -= 1

        cadena += "]"

        return f"""
{super().__str__()}

Historial Profesional:
=========================
Años de Experiencia:\t{self.aniosExperiencia}
Clubes:\t{cadena}"""
