
def say_hi():
    print("Hello user :D") 

say_hi()

# Definir una funcion con parametros 
def say_hile(name, age):
    print("Hello "+name+" you are "+age+" :D ")
        
# Se agrega como parametro un string en edad
say_hile("Elliot", "70")

# Definir una funcion pero en la entrada del parametro de edad en Int se agrega str() para convertirlo en texto 
def say_hola(name, age):
    print("Hello "+name+" you are "+str(age)+" :D ")

say_hola("Elliot", 70)

# Manera 1
# la funcion devulve el valor
def cube(num):
        return num*num
# Agrego el valor a una variable
result = cube(4)
# Imprime la variable
print(result)

# Manera 2
# La funcion devulve el una variable
def prueba(number):
        resultado = number*number
        return resultado
# Imprimo la funcion con sus paramtros
print(prueba(4))
