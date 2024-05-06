def merge_sort(arr, key):
    if len(arr) > 1:
        mitad = len(arr) // 2
        L = arr[:mitad]
        R = arr[mitad:]

        merge_sort(L, key)
        merge_sort(R, key)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][key] < R[j][key]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr
