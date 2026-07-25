a1 = int(input("Digite o valor onde a sequência vai começar: "))
n = int(input("Digite quantos números a sequência deve ter ao todo:"))
r = int(input("Digite o valor da razão: "))

ultimo_termo = a1 + (n * r)
for termo in range(a1, ultimo_termo, r):
    termo += r
    print(f"Resultado: {termo}", end=" ")
print("Fim")