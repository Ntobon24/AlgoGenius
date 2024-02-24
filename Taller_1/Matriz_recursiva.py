def recorrer_matriz(matriz, inicio_fila, fin_fila, inicio_columna, fin_columna):
    elementos = []

    if inicio_fila >= fin_fila or inicio_columna >= fin_columna:
        return elementos

    for i in range(inicio_fila, fin_fila):
        elementos.append(matriz[i][inicio_columna])

    for i in range(inicio_columna + 1, fin_columna):
        elementos.append(matriz[fin_fila - 1][i])

    if inicio_fila != fin_fila - 1:
            for i in range(fin_fila - 2, inicio_fila - 1, -1):
                elementos.append(matriz[i][fin_columna - 1])

    if inicio_columna != fin_columna - 1:
            for i in range(fin_columna - 2, inicio_columna, -1):
                elementos.append(matriz[inicio_fila][i])

    elementos += recorrer_matriz(matriz, inicio_fila + 1, fin_fila - 1, inicio_columna + 1,
                                 fin_columna - 1)

    return elementos

def matriz_espiral(matriz):
    if not matriz:
        return []
    return recorrer_matriz(matriz, 0, len(matriz), 0, len(matriz[0]))

