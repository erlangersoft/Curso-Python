class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado
    
    # Método getter
    def get_nombre(self):
        return self.__nombre
    
    # Método setter
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    def obtener_info(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"
