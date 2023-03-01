#pedir al usuario un numero entre 1-5, convertirlo a letras
"""
num = int(input("ingrese un numero entero del 1 al 5 para expresarlo en texto: "))

if num < 1 or num > 5:
    print("el número ingresado no está dentro del rango")
else:
    print
    if num == 1:
        print("el numero es Uno")
    elif num == 2:
        print("el numero es Dos")
    elif num == 3:
        print("el numero es Tres")
    elif num == 4:
        print("el numero es Cuatro")
    elif num == 5:
        print("el numero es Cinco")

#otra manera de hacerlo con una variable vacia, ejemplo: personas = " "
num = int(input("digite un num entre 1 y 5: "))
palabra = ""
if num == 1
    palabra = "Uno"
elif num == 2
    palabra = "Dos"
elif num == 1
    palabra = "Tres"
elif num == 1
    palabra = "Cuatro"
elif num == 1
    palabra = "Cinco"
else
    palabra = "error"
    
print(f"el numero {num} convertido es {palabra})
"""

#averiguar el estado de un semaforo e indicar un mensaje según el color
""""

print("1.Rojo 2.Naranja 3.Verde")
estado = int(input("ingrese el numero de acuerdo al color que ve: "))
             
if estado == 1:
    print("Detenga su vehiculo")
elif estado == 2:
    print("disminuya su velocidad")
elif estado == 3:
    print("Puede continuar")

#Hacerlo con string y utilizar lower y upper en el input, para cambiarlo desde la entrada
# lower() (pasar a minusculas)
# upper() (pasar a mayusculas)
"""
"""
estado = input("en qué color está el semáforo").lower()

if estado == "rojo":
    print("Detenga su vehiculo")
elif estado == "naranja":
    print("disminuya su velocidad")
elif estado == "verde": 
    print("Puede continuar")

"""

#un numero dado por pantalla es factor de 2 y 8. Si no es así, entonces multiplicarlo por 5 y averiguar si es factor de 10
# Recordar factor. Se divide un numero por otro y si el residuo da 0, es factor del divisor. 
# 8 % 2 = 0. 8 divido 2 da 4 y el residuo es 0, == 8 es factor de 2

                #caracteres de escape para todos los lenguajes. \ (backslash)

# \n, para salto de linea. Ejemplo:
#\t genera espacios para alinear datos. Ejemplo
#print("el resultado es:\t8\tlisto")
#print("el result es:\t\t5\tlisto")
#\' imprimir comillas sencillas dentro de sencillas
#\"" imprimir comillas dobles dentro de dobles  ("la buena \"nea\"...")
# \\, para que salga solo un \.

num = int(input("ingrese un numero entero positivo cualquiera:\n"))
if num < 0:
    print("el numero ingresado no es un entero positivo")
else:
    if num % 2 == 0 and num % 8 == 0:
        print("El número es factor de 2 y 8")
    else:
        num = num * 5
        if num % 10 == 0:
            print(f"si se multiplica el numero ingresado por 5 se convierte en {num} y se vuelve un factor de 10")
        else:
            print("el numero ingresado no es factor de 2 y 8. Al multiplicarlo por 5, tampoco es factor de 10")


