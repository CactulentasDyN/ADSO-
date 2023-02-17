#condicional anidado
#división 
num = int(input("ingrese cualquier número: "))

if num % 2 == 0:
    print("El número es par")
    if num < 0:
        print("y es un número negativo")
    else:
        print("y es un número positivo")
else:
    print("El número es impar")
    num = num * 3
    print(f"y multiplicado por 3 es: {num}")


    