from vehiculo import Vehiculo
from automovil import Automovil
from motocicleta import Motocicleta
from camion import Camion
import os # libreria con funciones del sistema operativo.

# Variables globales del sistema:
vehiculos = []
marca = ""
modelo = ""
anio = 0
nroPuertas = 0
nroPasajeros = 0
tipoMotor = ""
cilindrada = 0
nroRuedas = 0
torque = 0
capCarga = 0


# Definición de funciones del programa:
    
def mostrar_menu():
    os.system('cls') # Permite borrar el contenido de la consola.
    
    print("SISTEMA DE REGISTRO DE VEHÍCULOS")
    print("1. Listar Vehículos")
    print("2. Listar Automóviles")
    print("3. Listar Motocicletas")
    print("4. Listar Camiones")
    print("5. Registrar Nuevo")
    print("6. Eliminar")
    print("7. Registrar Personas")
    print("8. Asignar Propietario")
    print("9. Imprimir Información")
    print("0. SALIR")
    print("   Elija una opcion: ", end="")
    opcion = int(input())
    return opcion

def leerSubClasesVehiculo():
    subclasses = Vehiculo.__subclasses__()
    subclasses_names = []
    
    for subclass in subclasses:
        subclasses_names.append(subclass.__name__)
    
    for i in range(len(subclasses_names)):
        print(f"[{i+1}] {subclasses_names[i]}")

# Funcionalidades de la opción 1:
def opcion1():
    ##print(len(vehiculos))
    
    if not len(vehiculos) == 0:
        print("==============================")
        print("  LISTA GENERAL DE VEHÍCULOS  ")
        print("==============================")
        for i in range(0, len(vehiculos)):
            print("--------------------------------")
            print(f"\tRegistro Nro.: {i+1}")
            print(f"\tTipo:\t{type(vehiculos[i]).__name__}")
            print("--------------------------------")
            print(vehiculos[i])
    else:
        print("\n\033[91m<< Sin Registro de Vehículos. >>\033[0m")

# Funcionalidades de la opción 2:
def opcion2():
    if not len(vehiculos) == 0:
        
        print("==============================")
        print("     LISTA DE AUTOMÓVILES     ")
        print("==============================")
        
        for i in range(0, len(vehiculos)):
            
            if type(vehiculos[i]).__name__ == "Automovil":
                print("--------------------------------")
                print(f"\tRegistro Nro.: {i+1}")
                #print(f"\tTipo:\t{type(vehiculos[i]).__name__}")
                print("--------------------------------")
                print(vehiculos[i])
    else:
        print("\n\033[91m<< Sin Registro de Automóviles. >>\033[0m")

# Funcionalidades de la opción 3:
def opcion3():
    if not len(vehiculos) == 0:
        
        print("==============================")
        print("     LISTA DE AUTOMÓVILES     ")
        print("==============================")
        
        for i in range(0, len(vehiculos)):
            
            if type(vehiculos[i]).__name__ == "Motocicleta":
                print("--------------------------------")
                print(f"\tRegistro Nro.: {i+1}")
                #print(f"\tTipo:\t{type(vehiculos[i]).__name__}")
                print("--------------------------------")
                print(vehiculos[i])
    else:
        print("\n\033[91m<< Sin Registro de Motocicletas. >>\033[0m")

# Funcionalidades de la opción 4:
def opcion4():
    if not len(vehiculos) == 0:
        
        print("==============================")
        print("     LISTA DE AUTOMÓVILES     ")
        print("==============================")
        
        for i in range(0, len(vehiculos)):
            
            if type(vehiculos[i]).__name__ == "Camion":
                print("--------------------------------")
                print(f"\tRegistro Nro.: {i+1}")
                #print(f"\tTipo:\t{type(vehiculos[i]).__name__}")
                print("--------------------------------")
                print(vehiculos[i])
    else:
        print("\n\033[91m<< Sin Registro de Camiones. >>\033[0m")

# Funcionalidades de la opción 5:
def opcion5():
            
    print("==============================")
    print("   REGISTRAR NUEVO VEHÍCULO   ")
    print("==============================")
    
    leerSubClasesVehiculo()
    
    """subclasses = Vehiculo.__subclasses__()
    subclasses_names = []
    
    for subclass in subclasses:
        subclasses_names.append(subclass.__name__)
    
    for i in range(len(subclasses_names)):
        print(f"[{i+1}] {subclasses_names[i]}")"""# Mejor llevar todo a una función.
    
    print("Tipo de Vehículo: ", end="")
    tipo = int(input())
    
    if tipo == 1:
        # Leyendo datos generales de Vehículo:
        leerDatosGenerales()
        
        # Leyendo datos particulares de Automóvil:
        leerDatosAutomovil()
        
        # Instanciando Automovil:
        try:
            nuevoAutomovil = Automovil()
            nuevoAutomovil.marca = marca
            nuevoAutomovil.modelo = modelo
            nuevoAutomovil.anio = anio
            nuevoAutomovil.nroPuertas = nroPuertas
            nuevoAutomovil.nroPasajeros = nroPasajeros
            
            vehiculos.append(nuevoAutomovil)
            
            print("\033[95mAutomovil registrado correctamente...\033[0m\n")
            print(nuevoAutomovil)
        except ValueError as e:
            print(e)
            
    elif tipo == 2:
        # Leyendo datos generales de Vehículo:
        leerDatosGenerales()
        
        # Leyendo datos particulares de Motocicleta:
        leerDatosMotocicleta()
        
        # Instanciando Motocicleta:
        try:
            nuevaMotocicleta = Motocicleta()
            nuevaMotocicleta.marca = marca
            nuevaMotocicleta.modelo = modelo
            nuevaMotocicleta.anio = anio
            nuevaMotocicleta.tipoMotor = tipoMotor
            nuevaMotocicleta.cilindrada = cilindrada
            
            vehiculos.append(nuevaMotocicleta)
            
            print("\033[94mMotocicleta registrada correctamente...\033[0m\n")
            print(nuevaMotocicleta)
        except ValueError as e:
            print(e)
            
    elif tipo == 3:
        # Leyendo datos generales de Vehículo:
        leerDatosGenerales()
        
        # Leyendo datos particulares de Camión:
        leerDatosCamion()
        
        # Instanciando Camión:
        try:
            nuevoCamion = Camion()
            nuevoCamion.marca = marca
            nuevoCamion.modelo = modelo
            nuevoCamion.anio = anio
            nuevoCamion.nroRuedas = nroRuedas
            nuevoCamion.torque = torque
            nuevoCamion.capCarga = capCarga
            
            vehiculos.append(nuevoCamion)
            
            print("\033[96mCamión registrado correctamente...\033[0m\n")
            print(nuevoCamion)
        except ValueError as e:
            print(e)
    
    else:
        print("\033[91m<< Opción inválida >>\033[0m\n")
    

# Funcionalidades de la opción 6:
def opcion6():
    
    nroRegistros = len(vehiculos)
    print(f"Nro. de Registros: {nroRegistros}")
    
    nro = int(input("\nNro. de Registro a eliminar: "))
    
    if 1 <= nro <= nroRegistros:
        print("\033[96m")
        print("Datos de Registro a Eliminar:")
        print("------------------------------")
        print(vehiculos[nro - 1])
        print("\033[0m")
        
        print("\033[91m¿Confirma que desea eliminar el registro? [s][n]\033[0m")
        res = input()
        
        if res[0] == 's' or res[0] == 'S':
            try:
                vehiculos.remove(vehiculos[nro - 1])
                print("Registro eliminado correctamente.")
                
            except ValueError as e:
                print(e)
        
        nroRegistros = len(vehiculos)
        print(f"Nro. de Registros actualizado: {nroRegistros}")
    else:
        print("\033[92m<< No de realizaron cambios en el registro. >>\033[0m")

# Funcionalidades de la opción 7:
def opcion7():
    pass

# Funcionalidades de la opción 8:
def opcion8():
    pass

# Funcionalidades de la opción 9:
def opcion9():
    pass

# Función que lee los datos generales de un Vehículo:
def leerDatosGenerales():
    global marca
    print("Marca: ", end="")
    marca = str(input())
    
    global modelo
    print("Modelo: ", end="")
    modelo = str(input()) 
    
    global anio
    print("Año: ", end="")
    anio = int(input())

# Función que lee los datos específicos de un Automóvil:
def leerDatosAutomovil():
    global nroPuertas
    print("Nro. Puertas: ", end="")
    nroPuertas = int(input())
    
    global nroPasajeros
    print("Nro. Pasajeros: ", end="")
    nroPasajeros = int(input())

# Función que lee los datos específicos de una Motocicleta:
def leerDatosMotocicleta():
    global tipoMotor
    print("Tipo de Motor: ", end="")
    tipoMotor = input()
    
    global cilindrada
    print("Cilindrada: ", end="")
    cilindrada = int(input())

# Función que lee los datos específicos de un Camión:
def leerDatosCamion():
    global nroRuedas
    print("Nro. de Ruedas: ", end="")
    nroRuedas = input()
    
    global torque
    print("Torque: ", end="")
    torque = input()

    global capCarga
    print("Capacidad de Carga: ", end="")
    capCarga = input()
    
    
#----------------------------------------------------------------
# -- Inicio del Programa Principal: 
if __name__ == '__main__':
    
    # Vehículos de prueba:
    vehiculo1 = Automovil()
    vehiculo2 = Automovil("Toyota", "RAV-4", 2014, 4, 5)
    vehiculo3 = Motocicleta()
    vehiculo3.tipoMotor = "Motor Rotativo"
    vehiculo4 = Motocicleta("Honda", "Baja", 2000, "Motor de Combustión de Cuatro 4 tiempos", 250)
    vehiculo5 = Camion()
    vehiculo6 = Camion("Ford","F-150", 2015, 6, 265, 2500)
    
    # Añadiendo vehículos a una lista general.
    vehiculos.append(vehiculo1)
    vehiculos.append(vehiculo2)
    vehiculos.append(vehiculo3)
    vehiculos.append(vehiculo4)
    vehiculos.append(vehiculo5)
    vehiculos.append(vehiculo6)
    
    while True:        
        
        op = mostrar_menu()
        
        if op == 0:
            print("\n\033[33m<<Gracias por utilizar este programa.>>\033[0m")
            break
        elif op == 1:
            opcion1()
        
        elif op == 2:
            opcion2()
            
        elif op == 3:
            opcion3()
        
        elif op == 4:
            opcion4()
        
        elif op == 5:
            opcion5()
        
        elif op == 6:
            opcion6()
        
        elif op == 7:
            opcion7()
            
        elif op == 8:
            opcion8()
        
        elif op == 9:
            opcion9()
        
        print("\033[32m")
        os.system("Pause")
        print("\033[0m")

