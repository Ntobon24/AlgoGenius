import json


def insertion_sort_dict(arr, key):
    for i in range(1, len(arr)):
        key_value = arr[i]
        j = i - 1
        while j >= 0 and int(arr[j][key]) > int(key_value[key]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_value

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

#insertion_sort_dict(data, 'punt_lectura_critica')
#print(json.dumps(data, indent=4))