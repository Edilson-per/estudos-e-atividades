soma_salario_enfermeiro = 0.00
soma_salario_nutricionista = 0.00
soma_salario_medico = 0.00
num_nutricionistas = 0
num_medicos = 0
while True:
    print('''_____________________________________________________________
CÓDIGO CARGO
1 Enfermeiro
2 Nutricionista
3 Médico
0.encerrrar programa
_____________________________________________________________''')
    codigo = int(input("Digite o codigo relativo ao cargo: "))

    if codigo == 0:
        break
    elif codigo == 1:
        salario = float(input("Digite o sálario do funcionário: "))
        soma_salario_enfermeiro += salario
    elif codigo == 2:
        salario = float(input("Digite o sálario do funcionário: "))
        soma_salario_nutricionista += salario
        num_nutricionistas += 1
    elif codigo == 3:
        salario = float(input("Digite o sálario do funcionário: "))
        if salario > 4500:
            num_medicos += 1
    else:
        print(""" Por favor digite um código valido.
               
        """)

if num_nutricionistas > 0 :
    media = soma_salario_nutricionista / num_nutricionistas
    print(f"Essa é a média do salário dos nutricionistas: {media:.2f}")
else :
    print(f"Nenhum nutricionista cadastrado.")

print(f"Quantidade de médicos que recebem mais de R$ 4.500,00 de salário é: {num_medicos}")
print("Programa encerrado")




