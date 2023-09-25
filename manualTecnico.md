# Lenguajes Formales de Programaciòn
## Proyecto 1
### 2 do Semestre 2023
```js
Universidad San Carlos de Guatemala
Programador: Giovanni Saul Concohá Cax
Carne: 202100229
Correo: --
```
---
## Descripción
Se solicita la lectura de código fuente, el cual tendrá un formato JSON, creando un programa el cual sea capaz de identificar un lenguaje dado, identificando los errores léxicos y ejecutando las instrucciones correspondientes.
Se listarán una serie de instrucciones las cuales deben de ser ejecutadas, cumpliendo con el formato asignado, generándolo un resultado y graficarlos en un archivo según la jerarquía operacional de cada instrucción. Colocando el resultado en cada nodo que aplique. Los errores deben ser generados en un archivo JSON.

## Objetivos
* Objetivo General
    * Que el estudiante cree una herramienta la cual sea capaz de reconocer un lenguaje, dado por medio de un analizador léxico el cual cumple con las reglas establecidas, manejando la lectura y escritura de archivos para el manejo de la información. A través de un entorno gráfico.
* Objetivos Específicos
    * Implementar por medio de estados un analizador léxico.
    * Utilizar funciones de manejo de cadenas de caracteres en lenguaje Python.
    * Programar un Scanner para el análisis léxico.
    * Construir un scanner basándose en un autómata finito determinístico.
    * Crear una herramienta para interactuar de forma visual con el usuario con Tkinter
    * Crear diagramas con la librería Graphviz

---
## Analizador LEXICO

Este analizador procesa un texto de entrada y busca tokens y estructuras específicas en ese texto siguiendo una serie de estados y reglas definidas en los métodos del analizador.

Constructor (__init__): El constructor inicializa las propiedades básicas del analizador, como la entrada (self.lineas), el índice actual (self.index), la fila y la columna actuales, y una lista para almacenar errores (self.ListaErrores).

Método token: Este método se utiliza para analizar tokens específicos en el texto de entrada. Toma tres argumentos: token (el token que se busca), estadoActual (el estado actual del analizador) y estadoSig (el estado siguiente si se encuentra el token). Compara el token en la posición actual con el token buscado y avanza el índice si se encuentra una coincidencia.

Método juntar: Este método se utiliza para concatenar caracteres del texto de entrada en una cadena temporal (temp). Se utiliza en el método token para obtener el texto completo de un token.

Método analizar: Este método compara un token y un texto para verificar si coinciden. Compara cada carácter del texto con el token y devuelve True si coinciden y False si no lo hacen.

Método digito: Este método se utiliza para analizar números (dígitos) en el texto de entrada. Comienza en un estado inicial (D0) y avanza a través de los estados para reconocer números enteros y decimales.

Método operaciones: Este método se utiliza para analizar operaciones matemáticas y sus operandos en el texto de entrada. Utiliza varios estados y transiciones para reconocer la estructura de las operaciones matemáticas y sus componentes.

Método compilar: Este método es el punto de entrada principal para iniciar el análisis del texto de entrada. Utiliza varios estados para reconocer la estructura global del texto, que parece estar relacionado con la definición de operaciones matemáticas.

Método guardarErrores: Este método se utiliza para guardar información sobre errores encontrados durante el análisis en la lista self.ListaErrores. Registra el token, la fila y la columna donde se encuentra el error.


## Gramatica 
S0 -> { S01: La gramática comienza con una llave abierta "{" seguida de una producción "S01".

S01 -> "operaciones" S02: Después de la llave abierta, se espera encontrar la cadena "operaciones" seguida de la producción "S02".

S02 -> : S03: Luego, debe haber dos puntos ":" seguidos de "S03".

S03 -> [ S04: Se espera una llave cuadrada abierta "[" seguida de "S04".

S04 -> -> {S1: Aquí, se encuentra una flecha "->" que conduce a la producción "S1" y una llave abierta "{".

S1 -> "operacion" S2: "S1" representa una operación y comienza con la cadena "operacion" seguida de "S2".

S2 -> : S3: Luego, debe haber dos puntos ":" seguidos de "S3".

S3 -> OPERADOR S3_1: Se espera un operador, que se representa como "OPERADOR", seguido de "S3_1".

S3_1 -> , S4: "S3_1" permite una coma seguida de "S4", lo que indica la posibilidad de varios operadores en una operación.

S4 -> "valor1" S5: Aquí, se espera la cadena "valor1" seguida de "S5".

S5 -> : S6: Dos puntos ":" seguidos de "S6".

S6 -> DIGITO | [ S7: "S6" permite un dígito o una llave cuadrada abierta "[" seguida de "S7", lo que sugiere que "valor1" puede ser un dígito o una lista de valores.

S7 -> S0 S8: "S7" permite una referencia a "S0" seguida de "S8", lo que indica que puede haber una estructura anidada.

S8 -> ] S9: Se espera una llave cuadrada cerrada "]" seguida de "S9", lo que indica el final de "valor1".

S9 -> "valor2" S10: Luego, se espera la cadena "valor2" seguida de "S10".

S10 -> : S11: Dos puntos ":" seguidos de "S11".

S11 -> DIGITO | [ S12: "S11" permite un dígito o una llave cuadrada abierta "[" seguida de "S12", lo que sugiere que "valor2" puede ser un dígito o una lista de valores.

S12 -> S0 S13: "S12" permite una referencia a "S0" seguida de "S13", lo que indica la posibilidad de estructuras anidadas.

S13 -> ] S14: Se espera una llave cuadrada cerrada "]" seguida de "S14", lo que indica el final de "valor2".

S14 -> } }, S0 | S15: "S14" permite una llave cerrada "}" o dos llaves cerradas "}}" seguidas de una referencia a "S0" o "S15".

S15 -> ] S16: "S15" permite una llave cuadrada cerrada "]" seguida de "S16".

S16 -> } E: Finalmente, "S16" permite una llave cerrada "}" seguida de un símbolo Epsilon.


## Interfaz grafica
Es una interfaz gráfica básica para abrir, editar y guardar archivos de texto, así como realizar algunas operaciones específicas relacionadas con el análisis de contenido de archivo. 

Se importan las bibliotecas necesarias de tkinter y se crean algunas variables globales, como archivo_actual, que almacena la ruta del archivo actualmente abierto.

Se definen varias funciones para realizar acciones específicas:

abrirArchivo(): Abre un cuadro de diálogo de apertura de archivo y carga el contenido del archivo seleccionado en un panel de texto.

guardar(): Guarda el contenido actual en el archivo actualmente abierto o utiliza la función "Guardar como" si no hay un archivo actual.

guardar_como(): Abre un cuadro de diálogo de guardado de archivo y guarda el contenido del panel de texto en un archivo seleccionado.

cerrar_ventana(): Cierra la ventana de la aplicación.
seleccionar(event): Maneja la selección en un ComboBox y ejecuta diferentes funciones según la selección.

analizar(): Lee el contenido actual del panel de texto, crea un objeto analizador y llama a su método compilar para realizar algún tipo de análisis.

errores(): Función para manejar errores (a implementar según sea necesario).

reporte(): Función para generar un informe (a implementar según sea necesario).

Se crea la ventana principal (ventana) con un título y un tamaño específico.

Se crea un ComboBox (combo) que permite al usuario seleccionar entre varias opciones, como abrir, guardar, guardar como y salir.

Se crean botones para realizar acciones específicas, como analizar, manejar errores y generar un informe.

Se crea un panel de texto (panel_texto) donde se puede ver y editar el contenido del archivo.

Se asocia la función seleccionar(event) al evento <<ComboboxSelected>> del ComboBox para manejar las selecciones del usuario.

Se crea un botón "Cerrar" para cerrar la aplicación.

Finalmente, se ejecuta el bucle principal de Tkinter (ventana.mainloop()) para iniciar la aplicación y esperar las interacciones del usuario.
