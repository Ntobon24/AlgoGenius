def progresion_geometrica_recursiva(n):
    if n < 1:
        raise ValueError("El valor de 'n' debe ser un entero positivo mayor o igual a 1")
    
    if n == 1: 
        return 7
    else:
        return progresion_geometrica_recursiva(n - 1) * 2/5

def progresion_geometrica_no_recursiva(n):
    if n < 1:
        raise ValueError("El valor de 'n' debe ser un entero positivo mayor o igual a 1")
    
    termino_actual = 7  
    for i in range(2, n + 1):
        termino_actual *= 2/5  
    
    return termino_actual

try:
    n = int(input("Ingrese el valor de 'n': "))
    termino_100_recursivo = progresion_geometrica_recursiva(n)
    print("Recursivo:")
    print(f"El término {n} de la progresión geométrica es: {termino_100_recursivo}")
except ValueError as ve:
    print(f"Error en el cálculo recursivo: {ve}")

try:
    n = int(input("\nIngrese el valor de 'n': "))
    termino_100_no_recursivo = progresion_geometrica_no_recursiva(n)
    print("\nNo recursivo:")
    print(f"El término {n} de la progresión geométrica es: {termino_100_no_recursivo}")
except ValueError as ve:
    print(f"Error en el cálculo no recursivo: {ve}")