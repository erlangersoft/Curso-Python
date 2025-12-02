# Importando las clases creadas para el ejercicio:
from persona import Persona
from jugador import Jugador
from entrenador import Entrenador
from equipo import Equipo

# Creando un objeto de cada clase (Jugador, Entrenador y Persona):
Persona1 = Persona("Juan", "Cadima", "Fernandez", "10/10/1990", 1018217, 70456895,"Av. UCatec Nro. 18")
print(Persona1)

Jugador1 = Jugador("Pedro Alberto", "", "Guiberguis", "26/07/1969", 2784544, 72215487, "Calle Innominada Nro. 500", "Medio Campo", 10)
print(Jugador1)

entrenador1 = Entrenador("Vladimir","Soria", "Camacho", "15/07/1964", 458766, 72454877,"Tembladerani", 15)
print(entrenador1)

# Agregando clubes al entrenador:
#entrenador1.agregar_club("Bolivar")
#entrenador1.agregar_club("San José")
#print("Actualizando información:")
#print(entrenador1)

# Añadiendo objetos de tipo Equipo:
clubBolivar = Equipo("Bolivar")
print(clubBolivar)
clubSanto = Equipo("San José")
print(clubBolivar)

# Agregando clubes al Entrenador, utilizando objetos:
entrenador1.agregar_club(clubBolivar)
entrenador1.agregar_club(clubSanto)

print("Actualizando información:")
print(entrenador1)