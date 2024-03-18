from Taller_2.Model.Model import Formulas


def MenuPrincipal():

    #Complejidad temporal: O(1), espacial: O(1).
    while True:
        print("¿El orden en que se seleccionan los elementos importa? ")
        print("1. Si")
        print("2. No")A
        print("3. Salir a menu principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Ha seleccionado la opción 1")
            menuOrdenImporta()
        elif opcion == "2":
            print("Ha seleccionado la opción 2")
            MenuOrdenNoImporta()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def menuOrdenImporta():
    #Complejidad temporal: O(1), espacial: O(1).
    while True:
        print("¿Intervienen todos los elementos? ")
        print("1. Si")
        print("2. No")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Ha seleccionado la opción 1")
            OIIntervienenTodos()
            break
        elif opcion == "2":
            print("Ha seleccionado la opción 2")
            OINoIntervienenTodos()
            break
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def MenuOrdenNoImporta():
    #Complejidad temporal: O(1), espacial: O(1).
    while True:
        print("¿Se repiten elementos? ")
        print("1. Si")
        print("2. No")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Para la opción seleccionada se debe realizar una combinación con repetición")
            print("Ingresa la cantidad de elementos y de a cuanto se van a agrupar")
            n = int(input("Cantidad de elementos: "))
            r = int(input("Cantidad de elementos a agrupar: "))
            print(f"El resultado es: {Formulas.combinaciones_con_repeticion(n, r)}")
            break
        elif opcion == "2":
            print("Para la opción seleccionada se debe realizar una combinación sin repetición")
            print("Ingresa la cantidad de elementos y de a cuanto se van a agrupar")
            n = int(input("Cantidad de elementos: "))
            r = int(input("Cantidad de elementos a agrupar: "))
            print(f"El resultado es: {Formulas.combinaciones_sin_repeticion(n, r)}")
            break
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def OIIntervienenTodos():
    #Complejidad temporal: O(1), espacial: O(1).
    while True:
        print("¿Se repiten elementos? ")
        print("1. Si")
        print("2. No")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Para la opción seleccionada se debe realizar una permutación con repetición")
            print("Ingresa la cantidad de elementos y de a cuanto se van a agrupar")
            n = int(input("Cantidad de elementos: "))
            r = int(input("Cantidad de elementos a agrupar: "))
            print(f"El resultado es: {Formulas.permutaciones_con_repeticion(n, r)}")
            break
        elif opcion == "2":
            print("Para la opción seleccionada se debe realizar una permutación sin repetición")
            print("Ingresa la cantidad de elementos y de a cuanto se van a agrupar")
            n = int(input("Cantidad de elementos: "))
            r = int(input("Cantidad de elementos a agrupar: "))
            print(f"El resultado es: {Formulas.permutaciones_sin_repeticion(n, r)}")
            break
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def OINoIntervienenTodos():
    #Complejidad temporal: O(1), espacial: O(1).
    while True:
        print("¿Se repiten elementos? ")
        print("1. Si")
        print("2. No")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Para la opción seleccionada se debe realizar una variación con repetición")
            print("Ingresa la cantidad de elementos y de a cuanto se van a agrupar")
            n = int(input("Cantidad de elementos: "))
            r = int(input("Cantidad de elementos a agrupar: "))
            print(f"El resultado es: {Formulas.variaciones_con_repeticion(n, r)}")
            break
        elif opcion == "2":
            print("Para la opción seleccionada se debe realizar una variación sin repetición")
            print("Ingresa la cantidad de elementos y de a cuanto se van a agrupar")
            n = int(input("Cantidad de elementos: "))
            r = int(input("Cantidad de elementos a agrupar: "))
            print(f"El resultado es: {Formulas.variaciones_sin_repeticion(n, r)}")
            break
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

MenuPrincipal()
