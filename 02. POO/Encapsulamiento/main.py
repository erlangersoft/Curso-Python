from persona import Persona
# Crear un objeto Persona
persona = Persona("Juan", 30)

# Acceder a los atributos a través de métodos getter y setter
print(persona.get_nombre())  # Imprimirá "Juan"
persona.set_nombre("Carlos")
print(persona.get_nombre())  # Imprimirá "Carlos"

# Intentar acceder al atributo privado directamente generará un error
# print(persona.__nombre)  # Esto causará un AttributeError

# Llamar al método obtener_info
print(persona.obtener_info())  # Imprimirá "Nombre: Carlos, Edad: 30"
