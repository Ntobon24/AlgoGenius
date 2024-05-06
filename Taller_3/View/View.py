import json

from Taller_3.Model.Algoritmos.Insertion import insertion_sort
from Taller_3.Model.Algoritmos.Radix import radix_sort
from Taller_3.Model.Algoritmos.Bucket import bucket_sort
from Taller_3.Model.Algoritmos.Bubble import bubble_sort
from Taller_3.Model.Algoritmos.Selection import selection_sort
from Taller_3.Model.Algoritmos.MergeSort import merge_sort
from Taller_3.Model.Algoritmos.QuickSort import quick_sort
from Taller_3.Model.Algoritmos.HeapSort import heap_sort
from Taller_3.Model.Algoritmos.CountingSort import counting_sort

from Taller_3.Model.Model import data


def vista():
    columnas = {
        1: 'punt_global',
        2: 'punt_lectura_critica',
        3: 'punt_matematicas',
        4: 'punt_c_naturales',
        5: 'punt_sociales_ciudadanas',
        6: 'punt_ingles'
    }

    algoritmos = {
        1: insertion_sort,
        2: radix_sort,
        3: bucket_sort,
        4: bubble_sort,
        5: selection_sort,
        6: merge_sort,
        7: quick_sort,
        8: heap_sort,
        9: counting_sort
    }

    print("Columnas: 1-punt_global, 2-punt_lectura_critica, 3-punt_matematicas, 4-punt_c_naturales, 5-punt_sociales_ciudadanas, 6-punt_ingles")
    print("Algoritmos de ordenamiento: 1-Insercion, 2-Radix, 3-Bucket, 4-Burbuja, 5-Seleccion, 6-Merge Sort, 7-Quick Sort, 8-Heap Sort, 9-Counting Sort")

    columna = int(input("Elija una columna por la cual desea ordenar de la lista anterior (ingrese el número correspondiente): "))
    algoritmo = int(input("Elija un algoritmo de la lista anterior (ingrese el número correspondiente): "))

    if columna not in columnas or algoritmo not in algoritmos:
        print("Entrada no válida. Por favor, elija una opción de las listas proporcionadas.")
        return vista()

    print("Algoritmo utilizado:", list(algoritmos.keys())[algoritmo - 1])
    algoritmos[algoritmo](data, columnas[columna])
    print(json.dumps(data, indent=4))

vista()