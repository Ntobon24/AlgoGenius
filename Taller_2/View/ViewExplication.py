import tkinter as tk
from tkinter import ttk

def manejar_menu_principal():
    window = tk.Tk()
    window.title("Menú Principal")

    ttk.Label(window, text="Principios de Conteo", font=("Helvetica", 16, "bold")).pack(pady=10)
    ttk.Label(window, text="Seleccione una opción: -->", font=("Helvetica", 12)).pack()

    def opcion_seleccionada(opcion):
        if opcion == 1:
            mostrar_respuesta("¿Qué es un conteo?", "Un conteo es el acto de determinar la cantidad de elementos en un conjunto o la cantidad de resultados posibles en un experimento.")
        elif opcion == 2:
            window.destroy()
            manejar_menu_conteo()
        elif opcion == 3:
            window.destroy()
            manejar_menu_permutaciones_combinaciones()
        elif opcion == 4:
            tk.Label(window, text="¡Hasta luego!", font=("Helvetica", 12)).pack()
            window.destroy()

    ttk.Button(window, text="¿Qué es un conteo?", command=lambda: opcion_seleccionada(1)).pack(pady=5)
    ttk.Button(window, text="Principios básicos de conteo", command=lambda: opcion_seleccionada(2)).pack(pady=5)
    ttk.Button(window, text="Permutaciones, Combinaciones y Variaciones", command=lambda: opcion_seleccionada(3)).pack(pady=5)
    ttk.Button(window, text="Salir", command=lambda: opcion_seleccionada(4)).pack(pady=5)

    window.mainloop()