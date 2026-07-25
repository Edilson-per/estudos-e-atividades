num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma_num = num1 + num2
if num1 < num2 :
     menor = num1
else :
     menor = num2

fraseHUB = """
*********************************************
ESCOLHA UMA OPÇÃO ABAIXO:
*********************************************
1. Média ponderada, com pesos 2 e 3.
2. Quadrado da soma dos 2 números.
3 Cubo do menor número.

"""
print(fraseHUB)
escolha = int(input("Digite uma opção: "))

if escolha == 1 :
    media = ((num1 * 2) + (num2 * 3)) / (2 + 3)
    print(media)
elif escolha == 2:
    quadrado = soma_num ** 2
    print(f"A soma do quadrado dos dois números é : {quadrado}")
elif escolha == 3 :
    cubo_menor = menor ** 3
    print(f"Cubo do menor número é: {cubo_menor}")
else :
    print("Opção inválida")
