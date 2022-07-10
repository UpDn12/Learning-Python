

monthConversions = {
    0: "january",
    "Feb": "February",
    "Mar": "March",
}

# extrae la informacion de la KEY asignada
print(monthConversions[0])

# extrae la imforacion de la KEY asignida y si no esta agrega un comentario
print(monthConversions.get("lsa", "no es un valor"))
