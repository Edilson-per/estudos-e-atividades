escolha = int(input("""**** TABELA VERDADE ****
1. Operador AND
2. Operador OR
3. Operador NOT
**************************
Escolha uma opção: """))

if escolha not in [1, 2, 3] :
    print("Opção inválida.")
else:
    if escolha in [1, 2]:
        bit1 = int(input("Digite o bit1: "))
        bit2 = int(input("Digite o bit2: "))
        if bit1 not in [0 , 1] or bit2 not in [0 , 1] :
            print("Por favor digite apenas bit's válidos. 1 ou 0")
        else:
            if escolha == 1:
                resposta = bit1 and bit2
                print(f"Resultado:{resposta}")
            else :
                resposta = bit1 or bit2
                print(f"Resultado:{resposta}")
    else: 
        bit = int(input("Digite um bit: "))
        if bit not in [0 , 1]:
            print("Por favor digite apenas bit's válidos. 1 ou 0")
        else:
            resposta = 0 if bit == 1 else 1
            print(f"Resultado:{resposta}")
