# Definición de la clase Persona:

class Persona:
    nombre = None
    aPaterno = None
    aMaterno = None
    fechaNacimiento = None
    cedula = None
    telefono = None
    direccion = None

    # Métodos de la clase Persona:

    # -- Constructor --
    def __init__(self, nombre, aPaterno, aMaterno, fechaNacimiento, cedula, telefono, direccion) -> None:
        self.nombre = nombre
        self.aPaterno = aPaterno
        self.aMaterno = aMaterno
        self.fechaNacimiento = fechaNacimiento
        self.cedula = cedula
        self.telefono = telefono
        self.direccion = direccion
    
    def __str__(self) -> str:
        return f"""\
Información Personal:
=====================
Nombre: \t{self.nombre}
A. Paterno: \t{self.aPaterno}
A Materno: \t{self.aMaterno}
F. Nacimiento: \t{self.fechaNacimiento}
Cédula: \t{self.cedula}
Teléfono: \t{self.telefono}
Direción: \t{self.direccion}"""

        