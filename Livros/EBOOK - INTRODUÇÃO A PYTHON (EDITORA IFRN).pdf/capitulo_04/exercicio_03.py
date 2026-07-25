nome_mais_barato = ""
preco_mais_barato = 0.00
soma_precos = 0.00

for i in range(5):
    print(f"---{i + 1}° Medicamento ---")
    nome = input("Informe o nome do medicamento: ")
    preco = float(input("Informe o valor do medicamento: "))
    soma_precos += preco

    if  i == 0 or preco < preco_mais_barato:
        preco_mais_barato = preco
        nome_mais_barato = nome
    print()
media = soma_precos / 5

print("=" * 40)
print(f"Resultado: {media:.2f}")
print(f"O médicamento com o menor valor é: {nome_mais_barato}R$ {preco_mais_barato:.2f} ")

