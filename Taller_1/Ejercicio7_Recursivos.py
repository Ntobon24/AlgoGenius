#Equipo AlgoGenius
#Ejercicio 7 (Recursivo) - Nicolás Tobón, Santiago Giraldo, Matías Herrera

def suma_digitos(numero):
    if numero < 10:
        return numero
    else:
        ultimo_digito = numero % 10
        resto_numero = numero // 10
        return ultimo_digito + suma_digitos(resto_numero)
