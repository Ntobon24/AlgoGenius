def encontrar_minimo(lista):
    if len(lista) == 1:
        return lista [0]
    
    if len (lista) == 2:
        return min(lista[0], lista[1])
    
    mitad = len(lista) // 2
    mitad_izquierda = lista[:mitad]
    mitad_derecha = lista[mitad:]

    min_izquierda = encontrar_minimo(mitad_izquierda)
    min_derecha = encontrar_minimo(mitad_derecha)

    return min(min_izquierda , min_derecha)

lista = [3,7,2,8,55,5,4]
minimo = encontrar_minimo(lista)
print("El minimo de la lista es --> " , minimo)