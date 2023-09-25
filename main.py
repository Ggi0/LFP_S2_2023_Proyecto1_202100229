#Proyecto 1
#Lenguajes formales de programción 2S23
#Giovanni Saul Concohá Cax - 2021002292

import tkinter as tk
from tkinter import ttk

# Función para cerrar la ventana
def cerrar_ventana():
    ventana.destroy()

def seleccionar(event):
    seleccion = combo_var.get()

    if seleccion == "Salir":
        ventana.destroy()  # Cerrar la ventana

    resultado.config(text=f"Seleccionaste: {seleccion}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Proyecto 1")  # Título
ventana.geometry("800x600")  # Tamaño de la ventana

# Variable para almacenar la selección del ComboBox
combo_var = tk.StringVar()
# Valor inicial en el ComboBox
combo_var.set("ARCHIVO")

# ComboBox
combo = ttk.Combobox(ventana, textvariable=combo_var)
combo['values'] = ('Abrir', 'Guardar', 'Guardar como', 'Salir')
combo.pack(side="left", padx=10, pady=10)  # Empaquetar en la parte superior

# Botón "Guardar"
boton_guardar = tk.Button(ventana, text="Guardar")
boton_guardar.pack(side="left", padx=10)  # Empaquetar en la parte superior


# Botón "Abrir"
boton_abrir = tk.Button(ventana, text="Abrir")
boton_abrir.pack(side="left", padx=10)  # Empaquetar en la parte superior


# Crear un marco para alinear el panel de texto en la parte superior
marco_texto = tk.Frame(ventana)
marco_texto.pack(side="top", pady=20)

# Panel de texto centrado
panel_texto = tk.Text(marco_texto, width=100, height=20)  # Tamaño del panel de texto 100x100
panel_texto.pack(expand=True, fill="both", anchor="center")

# Asociar la función de selección al evento <<ComboboxSelected>>
combo.bind("<<ComboboxSelected>>", seleccionar)

# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="")
resultado.pack()

# Crear un marco para alinear el botón "Cerrar" en la parte inferior
marco_botones = tk.Frame(ventana)
marco_botones.pack(side="top", pady=10)  # Empaquetar en la parte superior

# Botón "Cerrar"
boton_cerrar = tk.Button(marco_botones, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack()

# Ejecutar el bucle principal de Tkinter
ventana.mainloop()


