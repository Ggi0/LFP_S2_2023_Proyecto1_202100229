'''
ruta = "/Users/gio/Desktop/LAB_LFP_2s23/Proyecto1/LFP_S2_2023_Proyecto1_202100229/text.json"
archivo = open(ruta, 'r')
lineas = ''
for i in archivo.readlines():
    lineas += i


text2_original = """{
    "operaciones":[
        {
            "operacion": "suma",
            "valor1": 4.5,
            "valor2": 2.3
        }
    ]
}
"""'''


class analizador:
    def __init__(self, entrada):
        self.lineas = entrada
        self.index = 0 #posicion del caracter
        self.fila = 1 #fila actual
        self.columna = 0 #columna actual
        self.ListaErrores = [] # LISTA PARA GUARDAR ERRORES

    #omitiendo los estados vacios
    def token(self, token:str , estadoActual: str, estadoSig:str):
        if self.lineas[self.index] != " ":
            print('\nLongitud del token',len(token),'\n')

            text = self.juntar(self.index, len(token))
            #print('junte -> ', text)

            if self.analizar(token, text):
                self.index += len(token) - 1
                self.columna += len(token) - 1
                return estadoSig
            else:
                return "ERROR"
        else:
            return estadoActual

    def juntar(self, index:int, contador:int):
        try:
            temp = ''
            #anidadar para juntar la palabra
            for i in range(index, index + contador):
                temp += self.lineas[i]
            return temp
        except:
            return None


    def analizar(self, token, texto):
        try:
            count = 0 
            token_tmp = ''
            
            for i in texto:
                #cuando la letra haga match con el token entra
                print(f'Comparando {i} == {token[count]}')
                if str(i) == str(token[count]):
                    token_tmp += i
                    count += 1
                else:
                    #print('error en Analizar')
                    return False
                
            print(f'\n----> Encontre: {token_tmp}')
            return True
        except:
            return False
        
    def digito(self, estadoSig):
        estadoActual = 'D0'
        numero = ""
        while self.lineas[self.index] != "":
            print(f'Caracter {self.lineas[self.index]} | ESTADO {estadoActual} | Fila: {self.fila} | Columna: {self.columna}')
            
            #  *** RESTRICCIONES ***

            #Identificar salto de linea para incrementar lineas
            if self.lineas[self.index]== "\n":
                self.fila+=1
                self.columna =0

            # para SALIR cuando encuentra una ","
            elif str(self.lineas[self.index]) == ',':
                self.index -= 1
                return [estadoSig, numero]
            
            elif str(self.lineas[self.index]) == '}':
                self.index -= 1
                return [estadoSig, numero]
            
            elif str(self.lineas[self.index]) == ']':
                self.index -= 1
                return [estadoSig, numero]

            # VERIFICAR SI ES DECIMAL
            elif self.lineas[self.index] == '.':
                token = "."
                if estadoActual == 'D2' or estadoActual == 'D0':
                    estadoActual = 'ERROR'
                elif self.lineas[self.index] != ' ':
                    text = self.juntar(self.index, len(token))
                    if self.analizar(token, text):
                        numero += text
                        estadoActual = 'D2'
                        self.index += len(token) - 1
                        self.columna += len(token) - 1
                    else:
                        estadoActual = 'ERROR'

            
            # ***** ESTADOS *****

            #D0 -> [1,2, ... ,9] D0 | D1
            elif estadoActual == "D0" or estadoActual == "D1":
                if self.lineas[self.index] != ' ':
                    estadoActual = "ERROR"
                    for i in ['0','1','2','3','4','5','6','7','8','9']:
                        token  = i
                        text = self.juntar(self.index, len(token))
                        if self.analizar(token, text):
                            numero += text
                            estadoActual = "D1"
                            break

            #D2 -> [1,2, ... ,9] D2 | D3
            elif estadoActual == "D2":
                if self.lineas[self.index] != ' ':
                    estadoActual = "ERROR"
                    for i in ['0','1','2','3','4','5','6','7','8','9']:
                        text = self.juntar(self.index, len(i))
                        if self.analizar(i, text):
                            numero += text
                            estadoActual = 'D2'
                            break


            # ***** ERRORES *****
            if estadoActual == "ERROR":
                print('--->> hubo un error <<---\n')
                return ['ERROR', -1]
            
            #incrementar posicion, leer caracter por caracter
            if self.index < len(self.lineas) -1:
                self.index += 1
            else:
                break


    #Desarrollo del ANALIZADOR
    def operaciones(self, estadoSig):
        estadoActual = 'S1'
        hijo_derecho = ""
        hijo_izquierdo = ""
        operador = ""

        while self.lineas[self.index] != '':
            #print(f'Caracter: {self.lineas[self.index]} | estado: {estadoActual} | Fila: {self.fila} | Columna: {self.columna}')
            
            #Identificar salto de linea para incrementar lineas
            if self.lineas[self.index]== "\n":
                self.fila += 1
                self.columna = 0
            

            # **** ESTADOS ****
            #-----------------token(token, estadoActual, estadoSig):
            # S1 -> "Operacion" S2
            elif estadoActual == 'S1':
                estadoActual = self.token('"operacion"', 'S1', 'S2')
            
            # S2 -> : S3
            elif estadoActual == 'S2':
                estadoActual = self.token(':', 'S2', 'S3')

            # S3 -> OPERADOR S3_1
            elif estadoActual == "S3":
                operadores = ['"suma"','"resta"','"multiplicacion"','"division"','"potencia"', '"inverso"', '"seno"', '"coseno"', '"tangente"', '"mod"']
                for i in operadores:
                    estadoActual = self.token(i, 'S3', 'S3_1')
                    if estadoActual != 'ERROR':
                        operador = i
                        break

            # S3_1 -> , S4
            elif estadoActual == 'S3_1':
                estadoActual = self.token(',', 'S3_1', 'S4')


            # S4 -> "valor1" S5
            elif estadoActual == 'S4':
                estadoActual = self.token('"valor1"', 'S4', 'S5')

            # S5 -> : S6
            elif estadoActual == 'S5':
                estadoActual = self.token(':', 'S5', 'S6')

            # S6 -> DIGITO  S9 | [ S7
            elif estadoActual == 'S6':
                estadoActual = self.token('[', 'S6', 'S6_1')
                if estadoActual == "ERROR":
                    estadoActual = 'S9'
                    a = self.digito('S9')
                    if "ERROR" == a[0]:
                        estadoActual = "ERROR"
                    elif a[0] == 'S9':
                        hijo_izquierdo = a[1]
                #estadoActual = self.digito("S6_1")

            # S6_1 -> , S7
            elif estadoActual == 'S6_1':
                estadoActual = self.token(',', 'S6_1', 'S7')

            # S7 -> S1 S8
            elif estadoActual == 'S7':
                a = self.operaciones('S8')
                estadoActual = a[0]
                hijo_izquierdo = a[1]

            # S8 -> ] S9
            elif estadoActual == 'S8':
                estadoActual = self.token(']','S8','S9')

            # S9 -> "valor2" S10
            elif estadoActual == 'S9':
                if operador == '"inverso"' or operador == '"seno"'or operador == '"raiz"'or operador == '"coseno"'or operador == '"tangente"':
                    self.index -= 1
                    # REALIZAR LA OPERACION ARITMETICA Y DEVOLVER UN SOLO VALOR
                    print("-----OPERACION ARITMETICA-----")
                    print(operador ,'(',hijo_izquierdo ,')' )
                    print('------------------------------\n')
                    op = operador +'('+hijo_izquierdo +')'
                    return ['S14', op]
                else:
                    estadoActual = self.token('"valor2"', 'S9', 'S10')
            
            # S10 -> : S11
            elif estadoActual == 'S10':
                estadoActual = self.token(':', 'S10', 'S11')

            # S11 -> DIGITO  S14 | [ S12
            #elif estadoActual == 'S11':
            elif estadoActual == 'S11':
                estadoActual = self.token('[','S11','S12')
                if estadoActual == 'ERROR':
                    estadoActual = 'S14'
                    a = self.digito('S14')
                    if "ERROR" == a[0]:
                        estadoActual = 'ERROR'
                    elif 'S14' == a[0]:
                        hijo_derecho = a[1]
                        # REALIZAR LA OPERACION ARITMETICA Y DEVOLVER UN SOLO VALOR
                        print("-----OPERACION ARITMETICA-----")
                        print(' ',hijo_izquierdo , operador, hijo_derecho)
                        print('------------------------------\n')
                        op = hijo_izquierdo + operador + hijo_derecho
                        return [estadoSig, op]
                #estadoActual = self.digito("S14")

            # S12 -> S1 S13
            elif estadoActual == 'S12':
                estadoActual = 'S13'
                a = self.operaciones('S13')
                hijo_derecho = a[1]
                if "ERROR" == a[0]:
                    estadoActual = 'ERROR'

            # S13 -> ] S14
            elif estadoActual == 'S13':
                estadoActual = self.token(']','S13','S14')

                # REALIZAR LA OPERACION ARITMETICA Y DEVOLVER UN SOLO VALOR
                print("-----OPERACION ARITMETICA-----")
                print(' ',hijo_izquierdo , operador, hijo_derecho)
                print('------------------------------\n')
                op = hijo_izquierdo + operador + hijo_derecho
                return [estadoSig, op]  

            '''# S14 -> }
            elif estadoActual == 'S14':
                print('estamos dentro de operaciones')
                estadoActual = self.token('}', 'S14', 'S15')'''

            

            # ***** ERRORES *****
            if estadoActual == "ERROR":

                self.guardarErrores(self.lineas[self.index], self.fila, self.columna)
                return ['ERROR', -1]
                #return "ERROR"
            
            #incrementar posicion, leer caracter por caracter
            if self.index < len(self.lineas) -1:
                self.index += 1
            else:
                break

    def compilar(self):
        estadoActual = 'S0' 
        while self.lineas[self.index] != '':
            print(f'Caracter: {self.lineas[self.index]} | estado: {estadoActual} | Fila: {self.fila} | Columna: {self.columna}')
            
            #Identificar salto de linea para incrementar lineas
            if self.lineas[self.index]== "\n":
                self.fila+=1
                self.columna =0
            
            # **** ESTADOS ****
            #-----------------token(token, estadoActual, estadoSig):
            # S0 -> { S01
            elif estadoActual == "S0":
                estadoActual = self.token('{', 'S0', 'S01')

            # S01 -> "operaciones" S02
            elif estadoActual == "S01":
                estadoActual = self.token('"operaciones"', 'S01', 'S02')

            # S02 -> : S03
            elif estadoActual == "S02":
                estadoActual = self.token(':', 'S02', 'S03')
            # S03 -> [ S04
            elif estadoActual == "S03":
                estadoActual = self.token('[', 'S03', 'S04')

            # S04 -> { S1
            elif estadoActual == "S04":
                estadoActual = self.token('{', 'S04', 'S1')

            # S1 -> "Operacion" S2
            elif estadoActual == 'S1':
                if self.lineas[self.index] != " ":
                    a = self.operaciones("S14")
                    estadoActual = a[0]
                    print('---RESULTADO---')
                    print(a[1])
                    print('---------------')
                #estadoActual = self.token('"operacion"', 'S1', 'S2')

            # S14 -> } 
            elif estadoActual == 'S14':
                print('estamos dentro de compilar')
                estadoActual = self.token('}', 'S14', 'S15')

            # S15 -> ,
            elif estadoActual == 'S15':
                if self.lineas[self.index] != ' ':
                    estadoActual = self.token(',', 'S16', 'S04')
            
            # S15 -> ] S16
            elif estadoActual == "S16":
                estadoActual = self.token(']', 'S16', 'S17')

            # S16 -> } S17
            elif estadoActual == "S17":
                estadoActual = self.token('}', 'S17', 'S18')

            elif estadoActual == 'S18':
                break


            # ***** ERRORES *****
            if estadoActual == "ERROR":
                print('--->> hubo un error <<---\n')
                estadoActual = "S04"
            
            #incrementar posicion, leer caracter por caracter
            if self.index < len(self.lineas) -1:
                self.index += 1
            else:
                break

    def guardarErrores(self, token, fila, columna):
        self.ListaErrores.append({"token":token, "fila": fila, "columna":columna})

'''
#print(lineas)

a = analizador(lineas)
#print(a.lineas)
a.compilar()

archivo.close()'''