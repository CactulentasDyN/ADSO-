
cantidad = int(input("Ingrese la cantidad de cds que desea comprar\n"))
costo_vendedor = 0.25

if cantidad >= 1 and cantidad <= 9:
    costo = 0.35

elif cantidad >= 10 and cantidad <= 99:
    costo = 0.34

    print(f"El precio")
elif cantidad >= 100 and cantidad <= 499:
    costo = 0.30

elif cantidad > 500:
    costo = 0.28

precio = costo * cantidad
costo_total = costo_vendedor * cantidad
ganancia = precio - costo_total

print(f"""
El precio de los cds para el cliente es {precio}.
El Costo para el vendedor es {costo_total} y su ganancia es {ganancia}
""")