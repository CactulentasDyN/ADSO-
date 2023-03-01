num = int(input("Ingrese un número entre el 1 y el 99:\n"))
if num < 1 or num > 99:
    print("El número ingresado no es válido")
else:
    if num > 0:
        print(f"El número {num} es positivo")
    else:
        print(f"El número {num} no es positivo")
    if num < 0:
        print(f"El numero {num} es negativo")
    else:
        print(f"El numero {num} no es negativo")
    if num % 2 == 0:
        print(f"El número {num} es par")
    else:
        print(f"El número {num} no es par")
    if num % 2 != 0:
        print(f"El número {num} es impar")
    else:
        print(f"El número {num} no es impar")
    if num % 3 == 0:
        print(f"El número {num} es factor de 3")
    else:
        print(f"El número {num} no es factor de 3")
    if num * num == 16:
        print(f"El numero {num} elevado a la 2 es 16")
    else:
        print(f"El número {num} elevado a la 2 no es 16")
    if num % 10 == 7:
        print(f"el numero {num} divido entre 10 tiene como residuo 7")
    else:
        print(f"el numero {num} divido entre 10 no tiene 7 de residuo")
    if num / 10 == 8:
        print(f"al dividir el numero {num} entre 10, obtenemos 8 como cociente ")
    else:
        print(f"al dividir el numero {num} entre 10, no obtenemos 8 como cociente")
