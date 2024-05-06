def counting_sort(arr, key):
    max_val = max(arr, key=lambda x: int(x[key]))
    max_val_int = int(max_val[key])
    count = [0] * (max_val_int + 1)

    for num in arr:
        count[int(num[key])] += 1

    output = []
    for i in range(len(count)):
        if count[i] > 0:
            for _ in range(count[i]):
                output.append(next(item for item in arr if int(item[key]) == i))
                output = arr

