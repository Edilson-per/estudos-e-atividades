maior_idade = 0
menor_idade = 0

while True :
    idade = int(input("Digite sua idade: "))

    if idade < 0:
        break
    elif maior_idade == 0 and menor_idade == 0 :
        maior_idade = idade
        menor_idade = idade
    else:
        if idade > maior_idade:
            maior_idade = idade
        elif idade < menor_idade:
            menor_idade = idade

media = (maior_idade + menor_idade) / 2

print(f"Essa é a média da menor e maior idade: {media:.2f}")

