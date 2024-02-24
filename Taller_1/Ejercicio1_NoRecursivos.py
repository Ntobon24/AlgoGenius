#Ejercicio 1 (No Recursivo)

def sumar_array(array):
    suma = 0
    for elemento in array:
        suma += elemento
    return suma

mi_arreglo = [1, 2, 3, 4, 5]
resultado = sumar_array(mi_arreglo)
print("La suma de los elementos del arreglo es:", resultado)