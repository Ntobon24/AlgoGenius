# Ejercicio 1
def factorizacion(n):
    factores = [0] * (n + 1)

    for i in range(2, n + 1):
        if factores[i] == 0:
            for j in range(i, n + 1, i):
                if factores[j] == 0:
                    factores[j] = i

    return factores


def factores_primos(n):
    factores = factorizacion(n)
    primos = []

    while n > 1:
        primos.append(factores[n])
        n //= factores[n]

    return primos


num = 15
print(f"Los factores primos de {num} son {factores_primos(num)}")
