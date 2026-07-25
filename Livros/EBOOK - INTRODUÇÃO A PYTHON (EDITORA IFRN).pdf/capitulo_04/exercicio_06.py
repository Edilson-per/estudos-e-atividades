menor_estatura = 0.00
maior_estatura = 0.00
soma_estatura = 0.00

for i in range(5):
    altura = float(input("Digite sua altura em (M): "))

    if i == 0:
        menor_estatura = altura
        maior_estatura = altura

        soma_estatura += altura

    else:
        if altura < menor_estatura:
            menor_estatura = altura
        elif altura > maior_estatura:
            maior_estatura = altura


