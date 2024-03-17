import math


class Formulas:

    @staticmethod
    def permutaciones_sin_repeticion(n, r):
        return math.factorial(n) // math.factorial(n - r)

    @staticmethod
    def permutaciones_con_repeticion(n, r):
        return n ** r

    @staticmethod
    def variaciones_sin_repeticion(n, r):
        return math.factorial(n) // math.factorial(n - r)

    @staticmethod
    def variaciones_con_repeticion(n, r):
        return n ** r
