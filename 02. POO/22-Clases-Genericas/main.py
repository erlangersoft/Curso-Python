from listagenerica import ListaGenerica
from os import system

system("cls")

lista_enteros = ListaGenerica()


lista_enteros.push(1)
lista_enteros.push(2)
lista_enteros.push(3)
lista_enteros.push(4)

#print(lista_enteros)
#print(f"Eliminando: {lista_enteros.pop()}")
#print(lista_enteros)


while True:
    system("cls")
    print("Listas Genéricas")
    print("1. Añadir Elemento")
    print("2. Borrar Elemento")
    print("3. Mostrar Lista")
    print("4. Salir")
    op = int(input("Elija una opción: "))
    
    if op == 1:
        elemento = input("Ingresar Elemento: ")
        lista_enteros.push(elemento)
        print("Cambios registrados:")
        print(lista_enteros)
        system("pause")
    elif op == 2:
        print(f"Eliminando: {lista_enteros.pop()}")
        system("pause")
    elif op == 3:
        print("Elementos de la lista genérica:")
        print(lista_enteros)
        system("pause")
    elif op == 4:
        system("cls")
        print("Gracias por utilizar este programa.")
        break
