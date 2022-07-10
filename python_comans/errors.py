


def Ecepciones():
    try:
        value = 10/0
        numero = int(input("pon un numeraco: "))
        print(numero)

    except ZeroDivisionError as err:
        print(err)

    except ValueError:
        print("Invelid input")

Ecepciones()