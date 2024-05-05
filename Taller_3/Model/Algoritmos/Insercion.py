import json


def insertion_sort(arr, key):
    for i in range(1, len(arr)):
        key_value = arr[i]
        j = i - 1
        while j >= 0 and int(arr[j][key]) > int(key_value[key]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_value

#insertion_sort(data, 'punt_lectura_critica')
#print(json.dumps(data, indent=4))