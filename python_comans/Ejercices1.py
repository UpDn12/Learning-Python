
def traducir (phrase):
    
    traduccion = ""
    for letter in phrase:
        
        if letter.lower() in "aeiou":
            traduccion = traduccion +"g"
        else:
           traduccion=traduccion+letter
    return traduccion

print(traducir(input("Enter a phrase: ")))