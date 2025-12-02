"""
--------------------------------
| Operador |     Descripción   |
--------------------------------
|    ==    | Igual que         |
|    !=    | Diferente         | 
|     <    | Menor que         |
|     >    | Mayor que         |
|    <=    | Menor o igual que |
|    >=    | Mayor o igual que |
--------------------------------
"""
## Ejemplo:
## Programa que calcula el mayor de tres numeros sin operadores lógicos.

while True:
    aux = input("Ingresa 3 números: ")
    a, b, c = aux.split(" ")
    a = int(a)
    b = int(b)
    c = int(c)

    # Controlar finalización:
    if a == 0 and b == 0 and c == 0:
        break
    else:
        if a == b:
            if a == c:
                print(f"Son Iguales a={a} b={b} c={c}")
            elif a > c:
                print(f"Mayores: a={a} y b={b}")
            else:
                print(f"Mayor: c={c}")
        elif a > b:
            if a == c:
                print(f"Mayores: a={a} y c={c}")
            elif a > c:
                print(f"Mayor: a={a}")
            else:
                print(f"Mayor: c={c}")
        elif b > a:
            if b == c:
                print(f"Mayores: b={b} y c={c}")
            elif b > c:
                print(f"Mayor: b={b}")
            else:
                print(f"Mayor: c={c}")

    