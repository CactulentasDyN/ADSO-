#condicional extenso. if - elif(condicion, sino si.) - else
#pedir nota de matematicas y muestre
#si la nota es menor que 3.5, perdió
#si la nota es menor que 4, Ganó de suerte.
#si la nota es mayor o igual que 4, felicitaciones!

nota = float(input("ingrese su nota de matematicas: "))
if nota < 3.5:
    print("perdió matemáticas")
elif nota < 4:
    print("pasó de chepaso")
else:
    print("Felicidades, Excelente nota")

#se puede utilizar and, or, not (cuando es necesario)
