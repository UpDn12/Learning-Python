
def while_funcion():
    # Ciclo While
    i=1
    while i<=10:
        print(i)
        i+=1 # i=i+1
    print("Done4 ")

def stupit_secret_word_game():
    secret_word="Helouda"
    guess=""
    i=1
    while guess != secret_word and i <=5:
        guess = input("enter guess: ")
        i+=1
    
    if guess==secret_word:
        print("you win!! :D")
    else:
        print("You lose :c")

def for_funcion_letra():
    #   Por cada letra en la palabra fisica se repitira
    for letter in "Fisica":
        print(letter)

def for_funcion_conLista():
    # len() devuleve la ubicacion de una lista
    friends = ["kennet", "julia", "susana"]
    # Imprime cada elemento de la lista
    for name in friends:
        print(name)
