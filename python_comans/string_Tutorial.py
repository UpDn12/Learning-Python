
def cadena_de_texto_basic():
    # Imprimir una cadena de texto
    print("Singularity")

    # Salto de una cadena te texto "como un enter"
    print("Singu\nlarity")

def variable_con_funciones():
    # Agregar una cadena de texto a una variables
    phrase = "Singularity"
    #         0123....

    # Imprimir una variable
    print(phrase)
    # Imprimir una variable y agregarle una cadean de texto
    print(phrase+" create")

    # Imprimir el texto en minusculas
    print(phrase.lower())

    # Imprimir el texto en mayusculas
    print(phrase.upper())

    # Comprobar si el terxto esta en mayusculas o en minusculas "Imprime un booleano"
    print(phrase.isupper())
    print(phrase.islower())

    # Colocar el texto en mayusculas y luego comprobar "Imprime un booleano"
    print(phrase.upper().isupper())

    # Indica cuanto numero de letras tiene el String
    print(len(phrase))

    # Indica que letra del string esta en esa posicion
    print(phrase[10])

    # Indica que la posicino de la letra que se indique "Arroja un numero"
    print(phrase.index("Sin"))

    # Reemplaza una "pedazo" del string por otro
    print(phrase.replace("Sin", "Cos"))

def ejercicio_de_string():
    #ejercicio de strings
    character_name = "Reberundo"
    character_age = "c"
    isMale = True

    print("huvo un hombre llamado " + character_name + ", ")
    print("el man tenia unos "+character_age+ " anos de edad xd")

    character_name = "Marco"
    print("el realmente le gustama el nombre de "+character_name+", era realmente genial")
    print("pero no le gustaba tener "+character_age+" anos :C")


