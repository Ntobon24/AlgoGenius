import math


class Formulas:

    @staticmethod
    def permutaciones_sin_repeticion(n, r):    #Complejidad temporal: O(n) , Complejidad espacial: O(1)
        return math.factorial(n) // math.factorial(n - r)

    @staticmethod
    def permutaciones_con_repeticion(n, r):    #Complejidad temporal: O(1) , Complejidad espacial: O(1)
        return n ** r

    @staticmethod
    def variaciones_sin_repeticion(n, r):    #Complejidad temporal: O(n) , Complejidad espacial: O(1)
        return math.factorial(n) // math.factorial(n - r)

    @staticmethod
    def variaciones_con_repeticion(n, r):    #Complejidad temporal: O(1) , Complejidad espacial: O(1)
        return n ** r

    @staticmethod
    def combinaciones_sin_repeticion(n, r):    #Complejidad temporal: O(n) , Complejidad espacial: O(1)
        return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

    @staticmethod
    def combinaciones_con_repeticion(n, r):    #Complejidad temporal: O(n) , Complejidad espacial: O(1)
        return math.factorial(n + r - 1) // (math.factorial(r) * math.factorial(n - 1))
