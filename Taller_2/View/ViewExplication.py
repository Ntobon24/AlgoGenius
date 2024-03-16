def mostrar_menu_principal():
    print("\nPrincipios de Conteo")
    print("Seleccione una opción: -->")
    print("\n1. ¿Qué es un conteo?")
    print("2. Principios básicos de conteo")
    print("3. Permutaciones, Combinaciones y Variaciones")
    print("4. Salir")
def mostrar_menu_conteo():
    print("\nPrincipios básicos de conteo:")
    print("Seleccione una opción: --> ")
    print("\n1. Principio de la suma")
    print("2. Principio del producto")
    print("3. Volver al menú principal")
def mostrar_menu_permutaciones_combinaciones():
    print("\nPermutaciones, Combinaciones y Variaciones:")
    print("Seleccione una opción: --> ")
    print("\n1. Permutaciones")
    print("2. Combinaciones")
    print("3. Variaciones")
    print("4. Volver al menú principal")
def manejar_menu_principal():
    while True:
        mostrar_menu_principal()
        opcion = input("\nIngrese el número de la opción deseada: ")
        if opcion == '1':
            print("\nHas seleccionado: ¿Qué es un conteo?")
            print("Respuesta: Un conteo es el acto de determinar la cantidad de elementos en un conjunto o la cantidad de resultados posibles en un experimento.")
        elif opcion == '2':
            manejar_menu_conteo()
        elif opcion == '3':
            manejar_menu_permutaciones_combinaciones()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
def manejar_menu_conteo():
    while True:
        mostrar_menu_conteo()
        opcion = input("\nIngrese el número de la opción deseada: ")
        if opcion == '1':
            print("\nHas seleccionado: Principio de la suma")
            print("Respuesta: El principio de la suma establece que si un evento puede ocurrir de m maneras diferentes y otro evento puede ocurrir de n maneras diferentes, y si los dos eventos no pueden ocurrir simultáneamente, entonces el total de maneras de que uno de los dos eventos ocurra es m + n.")
        elif opcion == '2':
            print("\nHas seleccionado: Principio del producto")
            print("Respuesta: El principio del producto establece que si un evento puede ocurrir de m maneras diferentes y otro evento puede ocurrir de n maneras diferentes, entonces el número total de maneras en que ambos eventos pueden ocurrir en secuencia es m * n.")
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
def manejar_menu_permutaciones_combinaciones():
    while True:
        mostrar_menu_permutaciones_combinaciones()
        opcion = input("\nIngrese el número de la opción deseada: ")
        if opcion == '1':
            print("\nHas seleccionado: Permutaciones")
            print("Respuesta: Las permutaciones son los distintos ordenamientos que se pueden hacer con los elementos de un conjunto.")
        elif opcion == '2':
            print("\nHas seleccionado: Combinaciones")
            print("Respuesta: Las combinaciones son subconjuntos de elementos de un conjunto, donde el orden de los elementos no importa.")
        elif opcion == '3':
            print("\nHas seleccionado: Variaciones")
            print("Respuesta: Las variaciones son selecciones ordenadas de elementos de un conjunto.")
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

manejar_menu_principal()
