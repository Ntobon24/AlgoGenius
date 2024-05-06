def heapify(arr, n, i, key):
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    if izquierda < n and arr[i][key] < arr[izquierda][key]:
        mayor = izquierda

    if derecha < n and arr[mayor][key] < arr[derecha][key]:
        mayor = derecha

    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        heapify(arr, n, mayor, key)


def heap_sort(arr, key):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i, key)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key)

    return arr