import tkinter as tk
from tkinter import ttk

# Función para manejar la selección en el ComboBox
def seleccionar(event):
    seleccion = combo_var.get()
    resultado.config(text=f"Seleccionaste: {seleccion}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("ComboBox en Tkinter")

# Crear una variable para almacenar la selección del ComboBox
combo_var = tk.StringVar()

# Crear el ComboBox
combo = ttk.Combobox(ventana, textvariable=combo_var)
combo['values'] = ('Opción 1', 'Opción 2', 'Opción 3', 'Opción 4')
combo.pack()

# Asociar la función de selección al evento <<ComboboxSelected>>
combo.bind("<<ComboboxSelected>>", seleccionar)

# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="")
resultado.pack()

# Ejecutar el bucle principal de Tkinter
ventana.mainloop()

