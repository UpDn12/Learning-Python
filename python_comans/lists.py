from ast import Num


def lista_basic():
    friends = [False, 2, "Kate", 5,"felipe", True]
    #           0     1     2.....
    #                           -3    -2    -1
    # Imprime la lista
    print(friends)

    # Imprime pa posicion indicada
    print(friends[2])

    # Imprime la lista de atras hacia delante
    print(friends[-2])

    # Imprime todo desde la posicion asignada
    print(friends[0:])

    #Imprime todo hasta la posicion asignada "sin contar la posicion 
    # asignada"
    print(friends[0:2])

    # modifica un elemto de la lista
    friends[1] = "Juan"

    print(friends[1])

def lista_funciones():
    lucky_numbers = [4, 8, 15, 16, 23, 42]
    amigos = ["kevin", "kevin","mathias","kaaren","tobbias"]

    # Agrega otra lista a la lista actial
    amigos.extend(lucky_numbers)

    # Agrega otro elemento a la lista actual "al final"
    amigos.append("kate")

    # Inserte un elemento en la posicion indicada y recorre los otros 
    # elementos
    amigos.insert(1, "Kelly")

    # Remueve un elemento de la lista, si esta en string deve colocarse en 
    # string
    amigos.remove("kevin")

    # Remueve todos los elementos de la lista
    amigos.clear()

    # Remueve el elemento que indiquemos
    amigos.pop(1)

    # Coloca la lista en orden acendente "menor a mayor en numeros y de 
    # A-Z"
    amigos.sort()

    # Coloca la lista al reves del ultimo elemento al primerp
    amigos.reverse()

def Copia_lista():
    amigos = ["pepe", "kevin", "kevin", "juan"]
    # Copia una lista a otra
    amigo = amigos.copy()

    print(amigo)

    # Indica la primera posicion que esta el elemento
    print(amigos.index("kevin"))

    # Indica cuantas veces se repite este elemnto
    print(amigos.count("kevin"))

def Lista_de_tuplas():
    # indica que solo hay un elemento en la lista "lista de tupples"
    coordinates = [(4, 5), (5, 1), (5, 8)]

    # tupples no pueden ser modificadas despues de ser creadas
    coordinates = (4, 5)

    print(coordinates)

def dosDList():

    numbers_grid =[
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [0]
    ]
    
    print(numbers_grid[2][1])

    for row in numbers_grid:
            print(row)

    for row in numbers_grid:
        for col in row:
            print(col)

dosDList()