#construir un algoritmo que convierta a positivo un número digitado por pantalla.
#numero = int(input("ingrese un número negativo cualquiera: "))
#numero2 = (numero * -1)
#print("el número expresado en positivo es: ", numero2)

# utilizando condicional
numero = int(input("ingrese un número negativo cualquiera: "))

if numero < 0:
    posit = numero * -1
    print(f"el numero positivo es: {posit}")
