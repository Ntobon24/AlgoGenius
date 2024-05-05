import json


def counting_sort(arr, digit, key):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    for i in range(size):
        index = int(arr[i][key]) // digit
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = int(arr[i][key]) // digit
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(size):
        arr[i] = output[i]


def radix_sort(arr, key):
    max_element = max([int(item[key]) for item in arr])
    digit = 1
    while max_element // digit > 0:
        counting_sort(arr, digit, key)
        digit *= 10



#radix_sort(data, 'punt_global')
#print(json.dumps(data, indent=4))
