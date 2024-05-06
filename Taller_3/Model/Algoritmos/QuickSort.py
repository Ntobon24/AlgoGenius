def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x[key] <= pivot[key]]
        greater_than_pivot = [x for x in arr[1:] if x[key] > pivot[key]]
        return quick_sort(less_than_pivot, key) + [pivot] + quick_sort(greater_than_pivot, key)

