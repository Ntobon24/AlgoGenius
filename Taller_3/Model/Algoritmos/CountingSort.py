def counting_sort(arr, key):
    max_val = max(arr, key=lambda x: x[key])
    count = [0] * (max_val[key] + 1)

    for num in arr:
        count[num[key]] += 1

    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i][key]] - 1] = arr[i]
        count[arr[i][key]] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]