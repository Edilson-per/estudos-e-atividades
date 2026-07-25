import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c
if delta < 0:
    print("Não existem raízes reais.")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    if delta == 0:
        print(f"A equação possui apenas uma raíz real: {x1}")

    else:
        print(f"A raízes reais são: x1 = {x1}, x2 = {x2}")