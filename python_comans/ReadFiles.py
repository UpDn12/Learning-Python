
from cgitb import text


def AbrirTextoBasic():
    # Abre un archivo 'r' para leer 'w' para escribir
    abrir = open('hola.txt', 'r')
    #   comprueba si se puede leer
    print(abrir.readable())
    # Lee todo el archivo
    print(abrir.read())

    abrir.close()

def LeerTextoLinea():
    abrir = open('hola.txt', 'r')
# Comprueba si se puede leer
    print(abrir.readable())
# Imprime la primera linea del texto y da un enter 
    print(abrir.readline())
    print(abrir.readline())

    abrir.close()

def LeerTextoLineas():
    abrir = open('hola.txt', 'r')
# Comprueba si se puede leer
    print(abrir.readable())
# Imprime las lineas en fomra de una lista 
    print(abrir.readlines())

    abrir.close()

def LeerTextoLineasIndice():
    abrir = open('hola.txt', 'r')
# Comprueba si se puede leer
    print(abrir.readable())
# Imprime la linea que se sindica 
    print(abrir.readlines()[1])

    abrir.close()

def LeerTextoLineasCicloFor():
    abrir = open('hola.txt', 'r')
# Imprime cada lina con un cilo for dando un enter entre linea
    for linea in abrir.readlines():
        print(linea)

    abrir.close()

#===============================================================================

def EscribirFinalTexto():
    Texto = open("hola.txt", "a")

    Texto.write("\nBebesito fiu fiu <3")

    Texto.close()

def EscribirTexto():
    # borra toda y escribe un texto
    texto1 = open("hola.txt", "w")

    texto1.write("\nConshatumare >:u")

    texto1.close()

def CrearTextoEscribir():
    texto1 = open("hola1.txt", "w")

    texto1.write("\nConshatumare >:u")

    texto1.close()


