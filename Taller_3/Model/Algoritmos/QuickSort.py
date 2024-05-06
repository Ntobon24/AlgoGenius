def quick_sort(arr, clave):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menor_que_pivote = [x for x in arr[1:] if x[clave] <= pivote[clave]]
        mayor_que_pivote = [x for x in arr[1:] if x[clave] > pivote[clave]]
        return quick_sort(menor_que_pivote, clave) + [pivote] + quick_sort(mayor_que_pivote, clave)