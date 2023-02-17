"""construye un programa que dados dos valores "x" y "y", verique si las siguientes ecuaciones arrojan el mismo resultado.

a) x + 3y
b) 2x-5y
Ejemplo:
x=16, y=2
x=8, y=1
x=0, y=0
x= -8, y= -1

"""
#Solucion ejercicio #1
"""
print("x+3y ; 2x-5y")
valorx = int(input("digite un valor para x: "))
valory = int(input("digite un valor para y: "))
ecu1 =  valorx + 3 * valory
ecu2 = 2 * valorx - 5 * valory
if ecu1 == ecu2:
    print("Correcto, Los valores ingresados hacen iguales ambas ecuaciones")
else:
    print("Incorrecto, las ecuaciones no dan el mismo resultado")


#Solución ejercicio #2

print("Para comparar qué hora es mayor, ingrese los siguientes datos:")

h1 = int(input("Digite la hora deseada: "))
m1 = int(input("Digite los minutos exactos: "))
mer1 = (input("Indique si la hora es AM o PM: "))

h2 = int(input("Digite la hora deseada: "))
m2 = int(input("Digite los minutos exactos: "))
mer2 = (input("Digite si la hora es AM o PM: "))

if mer1 == mer2:
    pass



else:
    if mer1 != mer2:
    
"""

# morí

#solucion ejercicio #3

h1 = int(input("ingrese una hora militar: "))
m1 = int(input("ingrese los minutos: "))

h2 = int(input("ingrese una hora militar: "))
m2 = int(input("ingrese los minutos: "))

if 0 < h1 < 24 and 0 < h2 < 24 and 0 < m1 < 59 and 0 < m2 < 59: 
    if h1 == h2 and m1 == m2:
        print(f"la primera hora {h1}:{m1} es igual a la segunda {h2}:{m2}") 
    elif h1 == h2 and m1 < m2:
        print(f"la primera hora {h1}:{m1} es menor que la segunda {h2}:{m2} ")
    elif h1 < h2:  
        print(f"la primera hora {h1}:{m1} es menor que la segunda {h2}:{m2}") 
    else:
        print(f"la segunda hora {h2}:{m2} es menor que la primera {h1}:{m1}")
else:
    print("La hora ingresada no es válida")


#solución ejercicio #4

num = float(input("ingrese un número decimal entre 1 y 10, para convertirlo en entero"))
ent = num
if 1 > num > 10:
    if num > .5:
        print()
#intentar con dec o con una funcion
else:
    print("El número ingresado no cumple los requerimentos solicitados")


#solución ejercicio #5
