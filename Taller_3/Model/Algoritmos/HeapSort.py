def heapify(arr, n, i, clave):
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    if izquierda < n and arr[i][clave] < arr[izquierda][clave]:
        mayor = izquierda

    if derecha < n and arr[mayor][clave] < arr[derecha][clave]:
        mayor = derecha

    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        heapify(arr, n, mayor, clave)


def heap_sort(arr, clave):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i, clave)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, clave)