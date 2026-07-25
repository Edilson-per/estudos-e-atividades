
while True:
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))


    if a >= b :
        print("Digite um valores válido")
    else :
        soma = 0
        for count in range (a, b + 1):
            soma += count

        print(f"Soma dos valores no intervalo [{a},{b}]: {soma}")
        break
