
"""construya un programa que lance 2 dados 4 veces
la suma de ambos, dio 3.
cuantas veces, la suma dió 5
cuantas veces, la suma dió 12
"""
cont5 = 0
cont12 = 0

import random
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
suma = dado1 + dado2
print(f"lanzada 1: dado 1: {dado1}, dado 2: {dado2}, Suma: {suma}")
if suma == 3:
    print("la suma de ambos dió 3")
elif suma == 5:
    cont5 = cont5 + 1
elif dado1 + dado2 == 12:
    cont12 = cont12 + 1


dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
suma = dado1 + dado2
print(f"lanzada 2: dado 1: {dado1}, dado 2: {dado2}, Suma: {suma}")
if suma == 3:
    print("la suma de ambos dió 3")
elif suma == 5:
    cont5 = cont5 + 1
elif dado1 + dado2 == 12:
    cont12 = cont12 + 1

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
suma = dado1 + dado2
print(f"lanzada 3: dado 1: {dado1}, dado 2: {dado2}, Suma: {suma}")
if suma == 3:
    print("la suma de ambos dió 3")
elif suma == 5:
    cont5 = cont5 + 1
elif dado1 + dado2 == 12:
    cont12 = cont12 + 1

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
suma = dado1 + dado2
print(f"lanzada 4: dado 1: {dado1}, dado 2: {dado2}, Suma: {suma}")
if suma == 3:
    print("la suma de ambos dió 3")
elif suma == 5:
    cont5 = cont5 + 1
elif dado1 + dado2 == 12:
    cont12 = cont12 + 1

print(f"la cantidad de veces que la suma dió 5 : {cont5}")
print(f"la cantidad de veces que la suma dió 12 : {cont12}")