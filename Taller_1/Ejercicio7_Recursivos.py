#Ejercicio 7 (Recursivo)

def suma_digitos(numero):
    if numero < 10:
        return numero
    else:
        ultimo_digito = numero % 10
        resto_numero = numero // 10
        return ultimo_digito + suma_digitos(resto_numero)

numero_entero = 12345
suma = suma_digitos(numero_entero)
print("La suma de los dígitos de", numero_entero, "es:", suma)