def recorrer_matriz(matriz, inicio_fila, fin_fila, inicio_columna, fin_columna):
    elementos = []

    if inicio_fila >= fin_fila or inicio_columna >= fin_columna:
        return elementos

    for i in range(inicio_fila, fin_fila):
        elementos.append(matriz[i][inicio_columna])

    for i in range(inicio_columna + 1, fin_columna):
        elementos.append(matriz[fin_fila - 1][i])