#Funciones 
import math

class Operaciones:
    num = [-2,45,4.6,-8.45,3.2] 
    #Suma de 2 o más números u operaciones anidadas.
    def suma(listNum):
        resultado = 0
        for i in listNum:
            resultado += i
        return round(resultado,2)
        #print('-> resultado final ', round(resultado,2))
        #62.800000000000004

    #Resta de 2 o más números u operaciones anidadas.
    def resta(lista1):
        resultado = lista1[0]  # Inicializamos el resultado con el primer elemento de la lista
        for i in range(1, len(lista1)):
            resultado -= lista1[i]
        return round(resultado,2)

    #Multiplicación de 2 o más números u operaciones anidadas.
    def multiplicacion(listNum):
        resultado = listNum[0]  # Inicializamos el resultado con el primer elemento de la lista
        for i in range(1, len(listNum)):
            resultado *= listNum[i]
        return round(resultado,2)

    #División entre números u operaciones anidadas.
    #num1 = numerador
    #num2 = denominador
    def division(num1, num2):
        if num2 == 0:
            return "la divison entre 0 no es posible"
        else:
            resultado = num1/num2

        return round(resultado,4)

    #Potencia N de un número u operación anidadas.
    #exp = exponente (enteros)
    def potencia(base, exp):
        resultado = math.pow(base, exp)
        return round(resultado, 2)

    #Raíz N de un número u operación anidadas.
    #num1 = radicando
    #num2 = indice
    def raiz(num1, num2):
        indice = 1/num2
        resultado = math.pow(num1, indice)
        return round(resultado, 2)

    #Inverso de un número u operación anidadas.
    '''es otro número que, cuando se multiplica por el número original, 
    produce un producto igual a 1'''
    def inverso(num1):
        inverso = 1 / num1
        return inverso
        pass

    #Función trigonométrica seno de un número u operación anidadas.
    def seno(angulo_grados):
        seno = math.sin(math.radians(angulo_grados))
        return round(seno, 4)

    #Función trigonométrica coseno de un número u operación anidadas.
    def coseno(angulo_grados):
        coseno = math.cos(math.radians(angulo_grados))
        return round(coseno,4)

    #Función trigonométrica tangente de un número u operación anidadas.
    def tangente(angulo_grados):
        tangente = math.tan(math.radians(angulo_grados))  # Calcula la tangente del ángulo en radianes
        return round(tangente,4)

    #Residuo entre números u operaciones anidadas.
    def mod(num1, num2):
        if num2 == 0:
            return "El valor no puede ser 0"
        else:
            resultado = num1 % num2
        return resultado 
        pass


'''
    print('\nSuma: ', suma(num))
    print('Resta: ', resta(num))
    print('Multiplicación ', multiplicacion(num))
    print('División ', division(15,3))
    print('potencia ', potencia(8,18))
    print('raiz ', raiz(98, 5))
    print('inverso ', inverso(35))
    print('Seno ', seno(82))
    print('Coseno ', coseno(30))
    print('tengente ', tangente(27))
    print('MOD: ', mod(15,3))
'''
