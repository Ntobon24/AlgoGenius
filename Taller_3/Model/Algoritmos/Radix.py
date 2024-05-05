import json


def counting_sort_dict(arr, digit, key):
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


def radix_sort_dict(arr, key):
    max_element = max([int(item[key]) for item in arr])
    digit = 1
    while max_element // digit > 0:
        counting_sort_dict(arr, digit, key)
        digit *= 10


data = [{
    "cole_nombre_establecimiento": "INSTITUCION EDUCATIVA CAMILO TORRES MOCARI",
    "punt_global": "295",
    "punt_lectura_critica": "60",
    "punt_matematicas": "65",
    "punt_c_naturales": "59",
    "punt_sociales_ciudadanas": "52",
    "punt_ingles": "59"
},
    {
        "cole_nombre_establecimiento": "INSTITUCION EDUCATIVA 1 DE MAYO",
        "punt_global": "209",
        "punt_lectura_critica": "49",
        "punt_matematicas": "44",
        "punt_c_naturales": "43",
        "punt_sociales_ciudadanas": "32",
        "punt_ingles": "40"
    },
    {
        "cole_nombre_establecimiento": "INSTITUCION EDUCATIVA POLITECNICO DE SOLEDAD",
        "punt_global": "244",
        "punt_lectura_critica": "57",
        "punt_matematicas": "35",
        "punt_c_naturales": "56",
        "punt_sociales_ciudadanas": "51",
        "punt_ingles": "38"
    },
    {
        "cole_nombre_establecimiento": "IE ANTONIO DE LA TORRE Y MIRANDA",
        "punt_global": "242",
        "punt_lectura_critica": "46",
        "punt_matematicas": "53",
        "punt_c_naturales": "46",
        "punt_sociales_ciudadanas": "46",
        "punt_ingles": "56"
    }
]

#radix_sort_dict(data, 'punt_global')
#print(json.dumps(data, indent=4))
