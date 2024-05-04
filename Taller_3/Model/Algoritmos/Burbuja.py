#Algoritmo burbuja sin implementar la API
def burbuja(columna):
    n = len(columna)
    for i in range(n):
        for j in range(0, n-i-1):
            if columna[j] > columna[j+1]:
                columna[j], columna[j+1] = columna[j+1], columna[j]
    return columna

# Ejemplo:
columna_api = [64, 34, 25, 12, 22, 11, 90]
print("Algoritmo de ordenamiento: Burbuja")
print("Columna original:", columna_api)
print("Columna ordenada:", burbuja(columna_api))


