#para reconocer cada acción/operación
from operaciones import Operaciones

class Operación():
    def __init__(self, operacion, valor1, valor2, listNum):
        self.operacion = operacion
        self.valor1 = valor1
        self.valor2 = valor2
        self.listNum = listNum

    def mostrarInfo(self):
        print('\n----------------')
        print('Operación: ', self.operacion)
        print('Valor1: ', str(self.valor1))
        print('Valor2: ' + str(self.valor2) +'\n----------------\n')

lista=[3,4,2]


objeto1 = Operación("suma",23,34,lista)
objeto1.mostrarInfo()

if objeto1.operacion == "suma":
    print(objeto1.operacion)
    list=[objeto1.valor1, objeto1.valor2]

    print('el resultado de la suma es ',Operaciones.suma(list) )