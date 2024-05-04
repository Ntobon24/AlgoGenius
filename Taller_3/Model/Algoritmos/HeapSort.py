def heapify(arr, n, i):
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    if izquierda < n and arr[i] < arr[izquierda]:
        mayor = izquierda

    if derecha < n and arr[mayor] < arr[derecha]:
        mayor = derecha

    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        heapify(arr, n, mayor)