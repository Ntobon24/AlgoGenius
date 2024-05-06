def counting_sort(arr, key):
    max_val = max(arr, key=lambda x: x[key])
    count = [0] * (max_val[key] + 1)

    for num in arr:
        count[num[key]] += 1

    output = []
    for i in range(len(count)):
        output.extend([i] * count[i])

    return output