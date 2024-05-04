#Algoritmo sin implementar la API
def bucket_sort(lista):
    # Crear un diccionario para almacenar las cubetas
    buckets = {}

    # Agregar elementos a las cubetas
    for num in lista:
        if num in buckets:
            buckets[num].append(num)
        else:
            buckets[num] = [num]

    # Ordenar las cubetas y concatenarlas
    sorted_list = []
    for key in sorted(buckets.keys()):
        sorted_list.extend(buckets[key])

    return sorted_list

#Ejemplo
lista = [64, 34, 25, 12, 22, 11, 90]
print("Algoritmo de ordenamiento: Bucket")
print("Lista original:", lista)
print("Lista ordenada:", bucket_sort(lista))

