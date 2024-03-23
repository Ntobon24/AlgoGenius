import tkinter as tk
from tkinter import ttk
from Taller_2.Model.Model import Formulas
# Complejidad temporal: O(1)
# Complejidad espacial: O(1)

def MenuPrincipal():
    window = tk.Tk()
    window.title("Menú Principal")
    window.geometry("400x200")

    style = ttk.Style()
    style.configure("Round.TButton", font=("Lato", 12), borderwidth=5, relief="raised", foreground="black",
                    background="#D3D3D3", padding=10, width=15, anchor="center")
    style.map("Round.TButton", foreground=[('pressed', 'black'), ('active', 'blue')])

    ttk.Label(window, text="¿El orden en que se seleccionan los elementos importa? ", font=("Lato", 12)).pack()
    ttk.Button(window, text="Si", command=menu_orden_importa, style="Round.TButton").pack(pady=5)
    ttk.Button(window, text="No", command=menu_orden_no_importa, style="Round.TButton").pack(pady=5)
    ttk.Button(window, text="Salir a menú principal", command=window.destroy, style="Round.TButton").pack(pady=5)

    window.mainloop()


def menu_orden_importa():
    window = tk.Tk()
    window.title("Menú de Orden (Importa)")
    window.geometry("300x200")

    style = ttk.Style()
    style.configure("Round.TButton", font=("Lato", 12), borderwidth=5, relief="raised", foreground="black",
                    background="#D3D3D3", padding=10, width=15, anchor="center")
    style.map("Round.TButton", foreground=[('pressed', 'black'), ('active', 'blue')])

    ttk.Label(window, text="¿Intervienen todos los elementos?", font=("Lato", 12)).pack()
    ttk.Button(window, text="Si", command=oi_intervienen_todos, style="Round.TButton").pack(pady=5)
    ttk.Button(window, text="No", command=oi_no_intervienen_todos, style="Round.TButton").pack(pady=5)
    ttk.Button(window, text="Salir", command=window.destroy, style="Round.TButton").pack(pady=5)

    window.mainloop()


def menu_orden_no_importa():
    window = tk.Tk()
    window.title("Menú de Orden (No Importa)")
    window.geometry("300x200")

    style = ttk.Style()
    style.configure("Round.TButton", font=("Lato", 12), borderwidth=5, relief="raised", foreground="black",
                    background="#D3D3D3", padding=10, width=15, anchor="center")
    style.map("Round.TButton", foreground=[('pressed', 'black'), ('active', 'blue')])

    ttk.Label(window, text="¿Se repiten elementos?", font=("Lato", 12)).pack()
    ttk.Button(window, text="Si", command=onii_se_repiten, style="Round.TButton").pack(pady=5)
    ttk.Button(window, text="No", command=onii_no_se_repiten, style="Round.TButton").pack(pady=5)
    ttk.Button(window, text="Salir", command=window.destroy, style="Round.TButton").pack(pady=5)

    window.mainloop()


def oi_intervienen_todos():
    window = tk.Tk()
    window.title("Menú de Orden (Importa) - Intervienen Todos")
    window.geometry("300x200")

    style = ttk.Style()
    style.configure("Round.TButton", font=("Lato", 12), borderwidth=5, relief="raised", foreground="black",
                    background="#D3D3D3", padding=10, width=15, anchor="center")
    style.map("Round.TButton", foreground=[('pressed', 'black'), ('active', 'blue')])

    ttk.Label(window, text="¿Se repiten elementos?", font=("Lato", 12)).pack()
    ttk.Button(window, text="Si", command=lambda: mostrar_resultado(Formulas.permutaciones_con_repeticion, "Permutaciones con Repetición"), style="Round.TButton").pack(pady=5)
    ttk.Button(window, text="No", command=lambda: mostrar_resultado(Formulas.permutaciones_sin_repeticion, "Permutaciones sin Repetición"), style="Round.TButton").pack(pady=5)
    ttk.Button(window, text="Salir", command=window.destroy, style="Round.TButton").pack(pady=5)

    window.mainloop()


def oi_no_intervienen_todos():
    window = tk.Tk()
    window.title("Menú de Orden (Importa) - No Intervienen Todos")
    window.geometry("300x200")

    style = ttk.Style()
    style.configure("Round.TButton", font=("Lato", 12), borderwidth=5, relief="raised", foreground="black",
                    background="#D3D3D3", padding=10, width=15, anchor="center")
    style.map("Round.TButton", foreground=[('pressed', 'black'), ('active', 'blue')])

    ttk.Label(window, text="¿Se repiten elementos?", font=("Lato", 12)).pack()
    ttk.Button(window, text="Si", command=lambda: mostrar_resultado(Formulas.variaciones_con_repeticion, "Variaciones con Repetición"), style="Round.TButton").pack(pady=5)
    ttk.Button(window, text="No", command=lambda: mostrar_resultado(Formulas.variaciones_sin_repeticion, "Variaciones sin Repetición"), style="Round.TButton").pack(pady=5)
    ttk.Button(window, text="Salir", command=window.destroy, style="Round.TButton").pack(pady=5)

    window.mainloop()


def onii_se_repiten():
    window = tk.Tk()
    window.title("Menú de Orden (No Importa) - Se Repiten Elementos")
    window.geometry("300x200")

    style = ttk.Style()
    style.configure("Round.TButton", font=("Lato", 12), borderwidth=5, relief="raised", foreground="black",
                    background="#D3D3D3", padding=10, width=15, anchor="center")
    style.map("Round.TButton", foreground=[('pressed', 'black'), ('active', 'blue')])

    ttk.Label(window, text="¿Se repiten elementos?", font=("Lato", 12)).pack()
    ttk.Button(window, text="Si", command=lambda: mostrar_resultado(Formulas.combinaciones_con_repeticion, "Combinaciones con Repetición"), style="Round.TButton").pack(pady=5)
    ttk.Button(window, text="No", command=lambda: mostrar_resultado(Formulas.combinaciones_sin_repeticion, "Combinaciones sin Repetición"),    style="Round.TButton").pack(pady=5)
    ttk.Button(window, text="Salir", command=window.destroy, style="Round.TButton").pack(pady=5)

    window.mainloop()


def mostrar_resultado(funcion, metodo):
    window = tk.Tk()
    window.title("Resultado")
    window.geometry("300x200")

    style = ttk.Style()
    style.configure("Round.TButton", font=("Lato", 12), borderwidth=5, relief="raised", foreground="black",
                    background="#D3D3D3", padding=10, width=15, anchor="center")
    style.map("Round.TButton", foreground=[('pressed', 'black'), ('active', 'blue')])

    ttk.Label(window, text="Ingrese la cantidad de elementos y de a cuanto se van a agrupar:", font=("Lato", 12)).pack(
        pady=10)

    entry_frame = ttk.Frame(window)
    entry_frame.pack(pady=5)

    ttk.Label(entry_frame, text="Cantidad de elementos:").grid(row=0, column=0, padx=5, pady=5)
    cantidad_entry = ttk.Entry(entry_frame)
    cantidad_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(entry_frame, text="Cantidad de elementos a agrupar:").grid(row=1, column=0, padx=5, pady=5)
    agrupar_entry = ttk.Entry(entry_frame)
    agrupar_entry.grid(row=1, column=1, padx=5, pady=5)

    resultado_label = ttk.Label(window, text="", font=("Lato", 12))
    resultado_label.pack(pady=5)

    def calcular():
        try:
            n = int(cantidad_entry.get())
            r = int(agrupar_entry.get())
            if n <= 0 or r <= 0:
                raise ValueError("Los valores deben ser mayores que cero.")
            if r > n:
                raise ValueError(
                    "La cantidad de elementos a agrupar no puede ser mayor que la cantidad total de elementos.")
            resultado = funcion(n, r)
            resultado_label.config(text=f"Método: {metodo}\nEl resultado es: {resultado}")
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                resultado_label.config(text="Error: Debe ingresar un número entero válido.")
            else:
                resultado_label.config(text=f"Error: {e}. Por favor, ingrese un valor válido.")

    ttk.Button(window, text="Calcular", command=calcular, style="Round.TButton").pack(pady=5)

    window.mainloop()


MenuPrincipal()

