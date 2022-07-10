def funcion_if_else():
    is_male = True
    is_tall = False
    # Declarar el if y else
    if is_male:
        print("sos un hombre mamalon")

    else:
        print("no sos un hombre :c")

def if_else_logica():
    is_male = True
    is_tall = False
    # Declara el "o"
    if is_male or is_tall:
        print("sos un hombre mamalon o sos un hombre alto")

    else:
        print("no sos ni hombre ni alto :c")

    # Declara el "y"
    if is_male and is_tall:
        print("sos un hombre mamalon o sos alto")

    else:
        print("no sos ni hombre ni alto :c")

def funcion_elif():
    is_male = True
    is_tall = False
    # Declara el elif
    if is_male and is_tall:
        print("sos un hombre mamalon y sos alto")
                    # Declara el not "si la variable no es vervadera entonces.."
    elif is_male and not(is_tall):
        print("sos un hombre bajito xd")

    elif not(is_male) and is_tall:
        print("no sos hombre pero sos alto felicidades :D")

    else:
        print("no sos hombre alto :c")
