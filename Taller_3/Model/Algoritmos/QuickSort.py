def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menor_que_pivote = [x for x in arr[1:] if x[key] <= pivote[key]]
        mayor_que_pivote = [x for x in arr[1:] if x[key] > pivote[key]]
        return quick_sort(menor_que_pivote, key) + [pivote] + quick_sort(mayor_que_pivote, key)