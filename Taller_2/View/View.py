import tkinter as tk
from tkinter import messagebox
from Taller_2.Model.Model import Formulas


class ViewExercise:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora combinaciones, variaciones y permutaciones")
        self.root.geometry("400x300")

        self.labels = [
            ("¿El orden en que se seleccionan los elementos importa? (s/n)", "orden"),
            ("¿Se repiten elementos en la selección? (s/n)", "repiten"),
            ("¿Entran todos los elementos disponibles? (s/n)", "todos")
        ]

        self.variables = {label_name: tk.StringVar(value="n") for _, label_name in self.labels}

        for label, label_name in self.labels:
            tk.Label(self.root, text=label).pack()
            entry = tk.Entry(self.root, textvariable=self.variables[label_name])
            entry.pack()

        self.button_calcular = tk.Button(self.root, text="Calcular técnica", command=self.calcular_tecnica)
        self.button_calcular.pack()

    def calcular_tecnica(self):
        inputs = {label_name: var.get() == 's' for label_name, var in self.variables.items()}
        tecnica = self.determinar_tecnica(**inputs)
        if tecnica:
            messagebox.showinfo("Técnica recomendada", f"La técnica recomendada es: {tecnica}")
            n = int(self.variables['n'].get())
            r = int(self.variables['r'].get())
            resultado = self.calcular_formula(tecnica, n, r)
            messagebox.showinfo("Resultado", f"El resultado es: {resultado}")

    def determinar_tecnica(self, orden_importa, elementos_se_repiten, todos_elementos_seleccionados):
        if todos_elementos_seleccionados:
            if orden_importa:
                return "Permutaciones con repetición" if elementos_se_repiten else "Permutaciones sin repetición"
            else:
                return "El orden sí importa para las permutaciones"
        else:
            if orden_importa:
                return "Variaciones con repetición" if elementos_se_repiten else "Variaciones sin repetición"
            else:
                return "Combinaciones con repetición" if elementos_se_repiten else "Combinaciones sin repetición"

    def calcular_formula(self, tecnica, n, r):
        if tecnica.startswith("Permutaciones"):
            return Formulas.permutaciones_con_repeticion(n, r) if "con" in tecnica else Formulas.permutaciones_sin_repeticion(n, r)
        elif tecnica.startswith("Variaciones"):
            return Formulas.variaciones_con_repeticion(n, r) if "con" in tecnica else Formulas.variaciones_sin_repeticion(n, r)
        else:
            return Formulas.combinaciones_con_repeticion(n, r) if "con" in tecnica else Formulas.combinaciones_sin_repeticion(n, r)


if __name__ == "__main__":
    vista = ViewExercise()
    vista.root.mainloop()
