import math

def calcular_raices(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        r1 = (-b + math.sqrt(discriminante)) / (2*a)
        r2 = (-b - math.sqrt(discriminante)) / (2*a)
    elif discriminante == 0:
        r1 = -b / (2*a)
        r2 = r1
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminante)) / (2*a)
        r1 = complex(real_part, imaginary_part)
        r2 = complex(real_part, -imaginary_part)
    return r1, r2

def calcular_coeficientes(a0, a1, r1, r2):
    if r1 == r2:
        k1 = a0
        k2 = (a1 - a0 * r1) / r1
    else:
        k2 = (a0 * r2 - a1) / (r2 - r1)
        k1 = a0 - k2
    return k1, k2

def obtener_formula(r1, r2):
    k2, k1 = calcular_coeficientes(a0, a1, r1, r2)
    if r1 == r2:
        formula = f"a_n = {k1} * {r1}**n + {k2} * n * {r1}**n"
    else:
        formula = f"a_n = {k1} * {r1}**n + {k2} * {r2}**n"
    return formula

def calcular_termino_n(a0, a1, r1, r2, n):
    try:
        k2, k1 = calcular_coeficientes(a0, a1, r1, r2)
        if r1 == r2:
            an = k1 * r1**n + k2 * n * r1**n
        else:
            an = k1 * r1**n + k2 * r2**n
        return an
    except OverflowError:
        return None

# Datos de entrada
while True:
    try:
        print("Ingrese los coeficientes de la ecuación de recurrencia (ax^2 + bx + c):")
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        ecuacion = f"{a}x**2 + {b}x + {c}"

        a0 = float(input("Ingrese el valor de a0: "))
        a1 = float(input("Ingrese el valor de a1: "))
        n = int(input("Ingrese el término n que desea calcular: "))
        break 
    except ValueError:
        print("Error: Por favor ingrese un número válido.")
        
# Calcular las raíces
r1, r2 = calcular_raices(a, b, c)
# Calcular el término enésimo
an = calcular_termino_n(a0, a1, r1, r2, n)
# Obtener la fórmula
formula = obtener_formula(r1, r2)

# Verificar si hubo overflow
if an is None:
    print("El resultado es demasiado grande para ser calculado numéricamente.")
    print("La fórmula es:")
    print(formula)
else:
    print(f"El término a_{n} es:", an)
