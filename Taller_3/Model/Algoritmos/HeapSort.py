def heapify(arr, n, i, key):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i][key] < arr[l][key]:
        largest = l

    if r < n and arr[largest][key] < arr[r][key]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)


def heap_sort(arr, key):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i, key)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key)