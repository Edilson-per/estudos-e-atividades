qtd_tentativas = 3
senha = 123456
nome = input("Digite seu nome: ")
while True:
    tentativa = int(input("Digite sua senha:"))
    if tentativa == senha:
        print(f"Olá{nome}, seja bem vindo ao nosso banco!")
    if tentativa != senha:
        print(f"Senha incorreta!Você ainda tem {qtd_tentativas - 1} tentativa(s)")
        qtd_tentativas -= 1
    if qtd_tentativas <= 0:
        print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas")
        break


