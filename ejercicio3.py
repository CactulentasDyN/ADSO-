nombre = input("ingrese su nombre:")

dias_trabajados = int( input("ingrese la cantidad de días que trabaja al mes:") )

horas_trabajadas = int( input("ingrese la cantidad de horas que trabaja al día:") )

sueldo_por_dia = horas_trabajadas * 5000

sueldo_total = sueldo_por_dia * dias_trabajados

print("El sueldo mensual de", nombre,"es de:", sueldo_total) 
