#Ejercicio #3 Fuerza Bruta
def min_sum_differences(A, B):
    min_sum = float('inf')
    n = len(A)
    
    # Función para generar todas las posibles permutaciones de los índices de B
    def generate_permutations(indices):
        nonlocal min_sum
        if len(indices) == n:
            sum_diff = sum(abs(A[i] - B[index]) for i, index in enumerate(indices))
            min_sum = min(min_sum, sum_diff)
            return
        for i in range(n):
            if i not in indices:
                generate_permutations(indices + [i])

    generate_permutations([])
    return min_sum

A = [4, 1, 8, 7]
B = [2, 3, 6, 5]
resultado = min_sum_differences(A, B)
print(f" El resultado es: {resultado}"