def recorrer_matriz(matriz, inicio_fila, fin_fila, inicio_columna, fin_columna):
    elementos = []

    if inicio_fila >= fin_fila or inicio_columna >= fin_columna:
        return elementos