import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Complejidad temporal: O(1)
# Complejidad espacial: O(1)

def abrir_menu_ejercicio():
    ventana.withdraw()
    import ViewExercise
    ViewExercise.menu_principal()
    ventana.deiconify()

def abrir_menu_explicacion():
    ventana.withdraw()
    import ViewExplication
    ViewExplication.manejar_menu_principal()
    ventana.deiconify()

def salir():
    if messagebox.askokcancel("Salir", "¿Estás seguro que quieres salir?"):
        ventana.destroy()

ventana = tk.Tk()
ventana.title("Menú Principal")
ventana.geometry("400x200")

style = ttk.Style()
style.configure("Round.TButton", font=("Lato", 12), borderwidth=5, relief="raised", foreground="black",
                background="#D3D3D3", padding=10, width=15, anchor="center")
style.map("Round.TButton", foreground=[('pressed', 'black'), ('active', 'blue')])

ttk.Label(ventana, text="Menú Principal", font=("Lato", 16, "bold")).pack(pady=10)

button_frame = ttk.Frame(ventana)
button_frame.pack(pady=20)

ttk.Button(button_frame, text="Hacer Ejercicio", command=abrir_menu_ejercicio, style="Round.TButton").pack(pady=5)
ttk.Button(button_frame, text="Ver Explicaciones", command=abrir_menu_explicacion, style="Round.TButton").pack(pady=5)
ttk.Button(button_frame, text="Salir", command=salir, style="Round.TButton").pack(pady=5)

ventana.mainloop()
