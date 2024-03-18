from Taller_2.Model.Model import Formulas


def MenuPrincipal():
    while True:
        print("¿El orden en que se seleccionan los elementos importa? ")
        print("1. Si")
        print("2. No")
        print("3. Salir")

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
    while True:
        print("¿Intervienen todos los elementos? ")
        print("1. Si")
        print("2. No")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Ha seleccionado la opción 1")
            OIIntervienenTodos()
        elif opcion == "2":
            print("Ha seleccionado la opción 2")
            OINoIntervienenTodos()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def MenuOrdenNoImporta():
    while True:
        print("¿Se repiten elementos? ")
        print("1. Si")
        print("2. No")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Ingresa la cantidad de elementos y de a cuanto se van a agrupar")
            n = int(input("Cantidad de elementos: "))
            r = int(input("Cantidad de elementos a agrupar: "))
            print(Formulas.combinaciones_con_repeticion(n, r))
        elif opcion == "2":
            print("Ingresa la cantidad de elementos y de a cuanto se van a agrupar")
            n = int(input("Cantidad de elementos: "))
            r = int(input("Cantidad de elementos a agrupar: "))
            print(Formulas.combinaciones_sin_repeticion(n, r))
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def OIIntervienenTodos():
    while True:
        print("¿Se repiten elementos? ")
        print("1. Si")
        print("2. No")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Ingresa la cantidad de elementos y de a cuanto se van a agrupar")
            n = int(input("Cantidad de elementos: "))
            r = int(input("Cantidad de elementos a agrupar: "))
            print(Formulas.permutaciones_con_repeticion(n, r))
        elif opcion == "2":
            print("Ingresa la cantidad de elementos y de a cuanto se van a agrupar")
            n = int(input("Cantidad de elementos: "))
            r = int(input("Cantidad de elementos a agrupar: "))
            print(Formulas.permutaciones_sin_repeticion(n, r))
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def OINoIntervienenTodos():
    while True:
        print("¿Se repiten elementos? ")
        print("1. Si")
        print("2. No")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Ingresa la cantidad de elementos y de a cuanto se van a agrupar")
            n = int(input("Cantidad de elementos: "))
            r = int(input("Cantidad de elementos a agrupar: "))
            print(Formulas.variaciones_con_repeticion(n, r))
        elif opcion == "2":
            print("Ingresa la cantidad de elementos y de a cuanto se van a agrupar")
            n = int(input("Cantidad de elementos: "))
            r = int(input("Cantidad de elementos a agrupar: "))
            print(Formulas.variaciones_sin_repeticion(n, r))
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
