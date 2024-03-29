# Equipo AlgoGenius
# Ejercicio 2 (No Recursivo) - Nicolás Tobón, Santiago Giraldo, Matías Herrera


#algoritmo euclidiano no recursivo para encontrar el MCD de dos números.
def algoritmo_euclidiano(a: int, b: int) -> int: # O(Log n), O(1)
    
    #b sea diferente de 0 porque sino habría division por cero.
    while b != 0: # O(Log n), O(1)

        # Se guarda el valor actual de b en una variable temporal.
        temp = b # O(1), O(1)

        # Se actualiza el valor de b al modulo(residuo) de a entre b.
        b = a % b # O(Log n), O(1)

        # Se actualiza el valor de a al valor anterior de b.
        a = temp # O(1), O(1)

    # Se retorna el valor final de a.
    return a # O(1), O(1)

#Llama a la funcion del Mcd y le pasa los dos parámetros
def encontrar_mcd_no_recursivo(a: int, b: int) -> int: # O(1), O(1)
    
    return algoritmo_euclidiano(a, b)

#Complejidad Temporal: O(Log n)
#Complejidad Espacial: O(1)
