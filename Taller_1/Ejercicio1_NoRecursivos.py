#Ejercicio 1 (No Recursivo)

def sumar_array(array): # O(n), O(1)
    suma = 0 # O(0), O(1)
    for elemento in array: # O(n), O(1)
        suma += elemento # O(n), O(1)
    return suma # O(0), O(1)

#Complejidad Temporal: O(n)
#Complejidad Espacial: O(1)