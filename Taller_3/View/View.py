import json

from Taller_3.Model.Algoritmos.Insercion import insertion_sort
from Taller_3.Model.Algoritmos.Radix import radix_sort
from Taller_3.Model.Algoritmos.Bucket import bucket_sort
from Taller_3.Model.Algoritmos.Burbuja import bubble_sort
from Taller_3.Model.Algoritmos.Seleccion import selection_sort
from Taller_3.Model.Algoritmos.CountingSort import counting_sort
from Taller_3.Model.Algoritmos.HeapSort import heap_sort
from Taller_3.Model.Algoritmos.QuickSort import quick_sort
from Taller_3.Model.Algoritmos.MergeSort import merge_sort

from Taller_3.Model.Model import data


def vista():
    columnas = {1: 'punt_global', 2: 'punt_lectura_critica', 3: 'punt_matematicas', 4: 'punt_c_naturales', 5: 'punt_sociales_ciudadanas', 6: 'punt_ingles'}
    algoritmos = {1: insertion_sort, 2: radix_sort, 3: bucket_sort, 4: bubble_sort, 5: selection_sort, 6: counting_sort, 7: heap_sort, 8: quick_sort, 9: merge_sort}

    print("Columnas: 1-punt_global, 2-punt_lectura_critica, 3-punt_matematicas, 4-punt_c_naturales, 5-punt_sociales_ciudadanas, 6-punt_ingles")
    print("Algoritmos de ordenamiento: 1-Insercion, 2-Radix, 3-Bucket, 4-Burbuja, 5-Seleccion, 6-Counting Sort, 7-Heap Sort, 8-Quick Sort, 9-Merge Sort")

    while True:
        try:
            columna = int(input("Elija una columna por la cual desea ordenar de la lista anterior (ingrese el número correspondiente): "))
            algoritmo = int(input("Elija un algoritmo de la lista anterior (ingrese el número correspondiente): "))
            if columna not in columnas or algoritmo not in algoritmos:
                print("Entrada no válida. Por favor, elija una opción de las listas proporcionadas.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    print("Algoritmo utilizado:", list(algoritmos.keys())[algoritmo - 1])
    algoritmos[algoritmo](data, columnas[columna])
    print(json.dumps(data, indent=4))


vista()
