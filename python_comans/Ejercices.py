
def calcularado_noob():
    # colocamos las variables con un input
    num_1 = input("Enter first number: ")
    num_2 = input("Enter second number: ")

    # sumamos las variables en formato stringg
    result = num_1 + num_2

    print(result)

    # sumamos las variables en formato de numero natural
    result = int(num_1) + int(num_2)

    print(result)

    # sumamos las variables en formato de numero real
    result = float(num_1) + float(num_2)

    print(result)

def juego_mad_libs_chafa():
    # ejercicio de mad libs chafa xd
    color = input("Enter a color: ")
    plural_noun = input("Enter a Plural noun: ")
    celebrity = input("Enter a celebrity: ")

    print("Roses are "+ color)
    print(plural_noun+ " are blue")
    print("I love " + celebrity)

def comparador_valores():
    # Operadores: == / != / 
    def max_num(num1, num2, num3):
        if num1 >= num2 and num1 >= num2:
            return num1
        elif num2 >= num1 and num2 >= num3:
            return num2
        else:
            return num3

    print("el numero mayor es: " + str(max_num(35,14,5)))

def traducir (phrase):
    
    traduccion = ""
    for letter in phrase:
        
        if letter.lower() in "aeiou":
            traduccion = traduccion +"g"
        else:
           traduccion=traduccion+letter
    return traduccion