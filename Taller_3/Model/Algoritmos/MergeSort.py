def merge_sort(arr, clave):
    if len(arr) > 1:
        medio = len(arr) // 2
        izquierda = arr[:medio]
        derecha = arr[medio:]

        merge_sort(izquierda, clave)
        merge_sort(derecha, clave)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i][clave] < derecha[j][clave]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1