#Proyecto 1
#Lenguajes formales de programción 2S23
#Giovanni Saul Concohá Cax - 2021002292

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog #abrir documentos
from reconcocerTexto import reconocerTexto
from analizadorClase import analizador

archivo_actual = None

#para abrir un archivo
def abrirArchivo():
    global archivo_actual
    #en ruta archivo se curado la ruta del archivo seleccionado
    ruta_archivo = filedialog.askopenfilename(title= "Abrir",filetypes=[("Archivos de texto", "*.*")])
    ruta_archivo = ruta_archivo.replace("\\", "/")
    if ruta_archivo:
        # Abrir y leer el archivo
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
        
        # Limpiar el panel de texto
        panel_texto.delete('1.0', tk.END)
        
        # Insertar el contenido del archivo en el panel de texto
        panel_texto.insert(tk.END, contenido)

        # Establecer el archivo actual
        archivo_actual = ruta_archivo

# Función para guardar el contenido en el archivo actual
def guardar():
    global archivo_actual
    if archivo_actual:
        contenido = panel_texto.get("1.0", "end-1c")  # Obtener el contenido del panel de texto
        with open(archivo_actual, 'w') as archivo:
            archivo.write(contenido)
    else:
        guardar_como()  # Si no hay archivo actual, utilizar la función "Guardar como"

    return(archivo_actual)


# Función para guardar Como el contenido del panel de texto en un archivo
def guardar_como():
    # Obtener el contenido del panel de texto
    contenido = panel_texto.get("1.0", "end-1c")  
    
    if contenido:
        ruta_guardar = filedialog.asksaveasfilename(filetypes=[("Archivos de texto", "*.*")])
        
        if ruta_guardar:
            # Guardar el contenido en el archivo seleccionado
            with open(ruta_guardar, 'w') as archivo:
                archivo.write(contenido)

# Función para cerrar la ventana
def cerrar_ventana():
    ventana.destroy()

# Funcion para realizar lo que diga el comboBox
def seleccionar(event):
    seleccion = combo_var.get()

    resultado.config(text=f"Seleccionaste: {seleccion}")
    if seleccion == "Abrir":
        print("abrir")
        abrirArchivo()

    if seleccion == "Guardar":
        print("Guardar")
        guardar()
        

    if seleccion == "Guardar como":
        print("Guardar como")
        guardar_como()
    
    if seleccion == "Salir":
        cerrar_ventana() # Cerrar la ventana

def analizar():
    print('Analizar')
    print(guardar())
    ruta = guardar()

    archivo = open(ruta, 'r')
    lineas = ''
    for i in archivo.readlines():
        lineas += i

    print(lineas)

    a = analizador(lineas)
    a.compilar()

    archivo.close()

    #contenido = panel_texto.get("1.0", "end-1c")  # Obtener el contenido del panel de texto

    #reconocerTexto(ruta_archivo)



def errores():
    print('errores')

def reporte():
    print('reporte')

# -----------------------------Ventana principal
ventana = tk.Tk()
ventana.title("Proyecto 1")  # Título
ventana.geometry("800x600")  # Tamaño de la ventana

# Variable para almacenar la selección del ComboBox
combo_var = tk.StringVar()
combo_var.set("ARCHIVO") # Valor inicial en el ComboBox

# marco para alinear el ComboBox y los botones en la parte superior
marco_superior = tk.Frame(ventana)
marco_superior.pack(side="top", pady=20)

# -----------------------------ComboBox
combo = ttk.Combobox(marco_superior, textvariable=combo_var)
combo['values'] = ('Abrir', 'Guardar', 'Guardar como', 'Salir')
combo.pack(side="left", padx=10)  # Empaquetar a la izquierda

# -----------------------------Botón "Analizar"
boton_guardar = tk.Button(marco_superior, text="Analizar", command=analizar)
boton_guardar.pack(side="left", padx=10)  # Empaquetar a la izquierda

# -----------------------------Botón "Errores"
boton_abrir = tk.Button(marco_superior, text="Errores", command=errores)
boton_abrir.pack(side="left", padx=10)  # Empaquetar a la izquierda

# -----------------------------Botón "Reporte"
boton_abrir = tk.Button(marco_superior, text="reporte", command=reporte)
boton_abrir.pack(side="left", padx=10)  # Empaquetar a la izquierda

# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="")
resultado.pack()

# marco para alinear el panel de texto en la parte de enMedio
marco_texto = tk.Frame(ventana)
marco_texto.pack(side="top", pady=20)

# -----------------------------Panel de texto centrado
panel_texto = tk.Text(marco_texto, width=100, height=20)  # Tamaño del panel de texto 100x100
panel_texto.pack(expand=True, fill="both", anchor="center")

# Asociar la función de selección al evento <<ComboboxSelected>>
combo.bind("<<ComboboxSelected>>", seleccionar)

# Marco para alinear el botón "Cerrar" en la parte inferior
marco_botones = tk.Frame(ventana)
marco_botones.pack(side="top", pady=10)  # Empaquetar en la parte superior

# -----------------------------Botón "Cerrar"
boton_cerrar = tk.Button(marco_botones, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack()



# Ejecutar el bucle principal de Tkinter
ventana.mainloop()



