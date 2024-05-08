import random

def matriz(n):
    tablero = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

    return tablero

def maximo_puntaje(tablero):
    if not tablero or not tablero[0]:
        return 0
        
    filas = len(tablero)
    columnas = len(tablero[0])
    puntos = 0
    i,j = 0,0
    
    while i < filas and j < columnas:
        puntos += tablero[i][j]
        if i == filas-1 and j == columnas-1:
            break
        elif i == filas-1:
            j+=1
            
        elif j == columnas-1:
            i+=1
            
        elif tablero[i+1][j] > tablero[i][j+1]:
            i+=1
        else:
            j+=1
                
    return puntos

def inicio():

    try:
        n = int(input("ingrese el tamaño de la matriz: "))
        tablero = matriz(n)
        print("Matriz generado:")

        for filas in tablero:
            print(filas)
            
        print("Puntos conseguidos")
        print(maximo_puntaje(tablero))

    except ValueError:
        print("Ingrese un valor valido")
        inicio()

inicio()