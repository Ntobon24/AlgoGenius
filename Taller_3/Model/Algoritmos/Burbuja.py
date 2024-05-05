def bubble_sort(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][key] > arr[j + 1][key]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
