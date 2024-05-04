#Algoritmo de Seleccion sin implementar la API
def seleccion(lista):
    n = len(lista)
    for i in range(n):
        # Encontrar el índice del mínimo elemento en el resto de la lista
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        
        # Intercambiar el mínimo encontrado con el primer elemento no ordenado
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    
    return lista

# Ejemplo:
lista = [64, 34, 25, 12, 22, 11, 90]
print("Algoritmo de ordenamiento: Seleccion")
print("Lista original:", lista)
print("Lista ordenada:", seleccion(lista))

