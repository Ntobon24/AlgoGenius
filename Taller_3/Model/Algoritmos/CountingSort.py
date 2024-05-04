def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    output = []
    for i in range(len(count)):
        output.extend([i] * count[i])

    return output