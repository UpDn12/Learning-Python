def numeros_basic():
    # Imprimir un numero
    print(2)

    # Imprimir un numero decimal
    print(2.52)

    # Imprimir un numero negativo
    print(-2)

    # Imprimir un numero por medio de operaciones
    print((2 + 3 - 4) * 5 / 5)

    # Imprimir el residuo de una divicion "lo que sobra de la divicion"
    print(5 % 2)

def variables_conFunciones():
    # Asignar un numero a una variable
    my_num = 416

    # Imprimir la variable
    print(my_num)

    # Imprimir la variable en forma de string para agregar mas texto
    print(str(my_num) + " number from gfl")

    # Asignar un numero negativo a una variable
    my_num = -15

    # Imprimir el valor absoluto de la variable
    print(abs(my_num))

    # Imprimir un numero elevado a otro
    #         (base,exponente)
    print(pow(my_num, 2))

    # Imprimir el mayor numero
    print(max(4, 6, 145, -2))

    # Imprimir el menor numero
    print(min(4, 6, 145, -2))

    # Redondear un numero
    print(round(3.5))

# Importar la clase math, se importa al principio del proyecto, no ahora xd
from math import *
def math_impport():

    # Convertir al numero siguiente
    print(floor(3.5))

    # Convertir al numero anterior
    print(ceil(3.5))

    #sacar la raiz
    print(sqrt(2))

# exponente ejemplos
def exponente(base_num, pow_num):
    result=1
    for index in range(pow_num):
        result=result*base_num
    return result

def exponente1(base_num, pow_num):
    result=base_num**pow_num
    return result


