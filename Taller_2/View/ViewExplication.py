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

def mostrar_respuesta(titulo, respuesta):
    respuesta_window = tk.Toplevel()
    respuesta_window.title(titulo)
    respuesta_window.geometry("400x200")

    ttk.Label(respuesta_window, text=titulo, font=("Helvetica", 14, "bold")).pack(pady=10)
    ttk.Label(respuesta_window, text=respuesta, wraplength=380, justify="left").pack(padx=20, pady=5)

def manejar_menu_conteo():
    window = tk.Tk()
    window.title("Menú de Conteo")

    ttk.Label(window, text="Principios básicos de conteo:", font=("Helvetica", 16, "bold")).pack(pady=10)
    ttk.Label(window, text="Seleccione una opción: -->", font=("Helvetica", 12)).pack()

    def opcion_seleccionada(opcion):
        if opcion == 1:
            mostrar_respuesta("Principio de la suma", "El principio de la suma establece que si un evento puede ocurrir de m maneras diferentes y otro evento puede ocurrir de n maneras diferentes, y si los dos eventos no pueden ocurrir simultáneamente, entonces el total de maneras de que uno de los dos eventos ocurra es m + n.")
        elif opcion == 2:
            mostrar_respuesta("Principio del producto", "El principio del producto establece que si un evento puede ocurrir de m maneras diferentes y otro evento puede ocurrir de n maneras diferentes, entonces el número total de maneras en que ambos eventos pueden ocurrir en secuencia es m * n.")
        elif opcion == 3:
            window.destroy()
            manejar_menu_principal()

    ttk.Button(window, text="Principio de la suma", command=lambda: opcion_seleccionada(1)).pack(pady=5)
    ttk.Button(window, text="Principio del producto", command=lambda: opcion_seleccionada(2)).pack(pady=5)
    ttk.Button(window, text="Volver al menú principal", command=lambda: opcion_seleccionada(3)).pack(pady=5)

    window.mainloop()

def manejar_menu_permutaciones_combinaciones():
    window = tk.Tk()
    window.title("Menú de Permutaciones, Combinaciones y Variaciones")

    ttk.Label(window, text="Permutaciones, Combinaciones y Variaciones:", font=("Helvetica", 16, "bold")).pack(pady=10)
    ttk.Label(window, text="Seleccione una opción: -->", font=("Helvetica", 12)).pack()

    def opcion_seleccionada(opcion):
        if opcion == 1:
            mostrar_respuesta("Permutaciones", "Las permutaciones son los distintos ordenamientos que se pueden hacer con los elementos de un conjunto.")
        elif opcion == 2:
            mostrar_respuesta("Combinaciones", "Las combinaciones son subconjuntos de elementos de un conjunto, donde el orden de los elementos no importa.")
        elif opcion == 3:
            mostrar_respuesta("Variaciones", "Las variaciones son selecciones ordenadas de elementos de un conjunto.")
        elif opcion == 4:
            window.destroy()
            manejar_menu_principal()

    ttk.Button(window, text="Permutaciones", command=lambda: opcion_seleccionada(1)).pack(pady=5)
    ttk.Button(window, text="Combinaciones", command=lambda: opcion_seleccionada(2)).pack(pady=5)
    ttk.Button(window, text="Variaciones", command=lambda: opcion_seleccionada(3)).pack(pady=5)
    ttk.Button(window, text="Volver al menú principal", command=lambda: opcion_seleccionada(4)).pack(pady=5)

    window.mainloop()

manejar_menu_principal()