"""Preguntar  al usuario su deporte favorito
    1. Fútbol
    2. Voley
    3. Basquet
    4. Sóftbol
    Preguntarle al usuario si tiene x cantidad de jugadores para que responda True/False. Decirle si acertó o no.

"""

print("1.Fútbol 2.Voley 3.Basquet 4.Sóftbol")
dep = int(input("¿Cual de los anteriores es su deporte favorito?: "))
if dep == 1: 
    res = input("¿el deporte tiene 11 jugadores?: ")    
    if res == "Si":
        print("Es correcto")
    else:
        print("La respuesta es incorrecta")
elif dep == 2:
    res = input("¿El deporte tiene 6 jugadores?: ")    
    if res == "Si":
        print("Es correcto")
    else:
        print("La respuesta es incorrecta")
elif dep == 3:
    res = input("¿El deporte tiene 5 jugadores?: ")    
    if res == "Si":
        print("Es correcto")
    else:
        print("La respuesta es incorrecta")
elif dep == 4:
    res = input("¿El deporte tiene 10 jugadores?: ")    
    if res == "si":
        print("Es correcto")
    else:
        print("La respuesta es incorrecta")
else:
    print("Error, deporte no incluido")
