class ValorPermitido:
    VALORES_PERMITIDOS = ["valor1", "valor2", "valor3"]

    def __init__(self, valor):
        if valor in self.VALORES_PERMITIDOS:
            self.valor = valor
        else:
            raise ValueError(f"El valor debe ser uno de {self.VALORES_PERMITIDOS}")

class MiClase:
    def __init__(self, valor):
        self.atributo = ValorPermitido(valor)

# Crear una instancia de MiClase con un valor permitido
objeto1 = MiClase("valor1")
print(objeto1.atributo.valor)  # Imprimirá "valor1"

# Intentar crear una instancia de MiClase con un valor no permitido
try:
    objeto2 = MiClase("valor4")  # Esto generará un ValueError
except ValueError as e:
    print(e)  # Imprimirá el mensaje de error