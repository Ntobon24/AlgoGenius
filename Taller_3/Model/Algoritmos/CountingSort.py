def counting_sort(arr, clave):
    max_val = max(arr, key=lambda x: x[clave])
    cuenta = [0] * (max_val[clave] + 1)

    for num in arr:
        cuenta[num[clave]] += 1

    salida = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        salida[cuenta[arr[i][clave]] - 1] = arr[i]
        cuenta[arr[i][clave]] -= 1

    for i in range(len(arr)):
        arr[i] = salida[i]