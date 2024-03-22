from Taller_2.View.ViewExercise import MenuPrincipal
from Taller_2.View.ViewExplication import manejar_menu_principal


def Menu():
    #Complejidad temporal: O(n), Complejidad espacial: O(1),
    
    print("Seleccione una opción: ")
    print("1. Explicacion")
    print("2. Realizar ejercicio")

    while True:
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            manejar_menu_principal()
        elif opcion == "2":
            MenuPrincipal()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
