# Equipo AlgoGenius
# Ejercicio 2 (No Recursivo)

def algoritmo_euclidiano(a, b):
    
    while b != 0:

        temp = b

        b = a % b

        a = temp
        
    return a

def encontrar_mcd_no_recursivo(a, b):

    return algoritmo_euclidiano(a, b)


numero1 = 48
numero2 = 18
mcd = encontrar_mcd_no_recursivo(numero1, numero2)
print("El MCD de", numero1, "y", numero2, "es:", mcd)