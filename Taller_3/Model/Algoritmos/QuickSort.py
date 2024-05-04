def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menor_que_pivote = [x for x in arr[1:] if x <= pivote]
        mayor_que_pivote = [x for x in arr[1:] if x > pivote]
        return quick_sort(menor_que_pivote) + [pivote] + quick_sort(mayor_que_pivote)