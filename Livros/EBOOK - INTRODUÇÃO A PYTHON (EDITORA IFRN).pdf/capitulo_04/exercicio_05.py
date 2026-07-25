melhor_tempo = 0
pior_tempo = 0
melhor_nadador = ""
pior_nadador = ""
total_tempo = 0.00
atletas_tempo = 0
for i in range(5):
    nome = input("Digite seu nome: ")
    tempo = float(input("Digite o tempo em (s): "))
    total_tempo += tempo

    if i == 0 :
        melhor_nadador = nome
        pior_nadador = nome

        melhor_tempo = tempo
        pior_tempo = tempo
    else :
        if tempo < melhor_tempo:
            melhor_nadador = nome
            melhor_tempo = tempo

        elif tempo > melhor_tempo:
            pior_nadador = nome
            pior_tempo = tempo



    if 12 >= tempo >= 15 :
        atletas_tempo += 1

media = total_tempo / 7

print("-"*40)
print(f"Esse foi o atleta com o melhor tempo: {melhor_nadador}")
print("-"*40)
print(f"Esse foi o atleta com pior tempo: {pior_nadador}")
print("-"*40)
print(f"Esse é o tempo medio dos nadadores: {media:.2f}")
print("-"*40)
print(f"Essa é a quantidade de atletas entre (12s) e (15s): {atletas_tempo}")




