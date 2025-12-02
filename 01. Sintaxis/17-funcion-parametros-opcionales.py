# Parametros opcionales:
def getEmpleado(nombre, ci = None):
    print(f"Nombre: {nombre}")
    
    if ci is not None:
        print(f"Cedula: {ci}")


getEmpleado("Juan Calderón")
getEmpleado("Jose Zago", "21545")