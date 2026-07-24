# ------------------------------------------------------------------------------
# EXERCÍCIO 02
# ------------------------------------------------------------------------------

'''2. Para construir o programa a seguir, considere que os usuários só informarão números inteiros positivos. Crie um programa que receba 5 números digitados e, ao fim, exibir quantos
números são pares.'''

pares = 0
for count in range (5):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        pares += 1

print(f"Essa é a quantidade de números pares: {pares}")


# ------------------------------------------------------------------------------
# EXERCÍCIO 03
# ------------------------------------------------------------------------------

"""3. Construa um programa para fazer uma pequena entrevista com
os alunos de uma turma. Na entrevista, são informados o sexo e
a idade de cada aluno. Considere que o usuário não sabe quantos alunos existem na turma. O programa deve exibir a quantidade de homens acima de 18 anos e a quantidade de mulheres de
qualquer idade. Para encerrar o programa, o usuário deve informar uma idade negativa."""

alunoH = 0
alunoF = 0

while True :
    idade = int(input("Digite sua idade: "))
    if idade < 0:
        break

    sexo = str(input("Digite seu sexo (M/F): "))
    if sexo == "F" or sexo == "f":
        alunoF += 1

    elif sexo == "M" or  sexo == "m":
        if idade >= 18:
            alunoH += 1

print(f"Total de mulheres: {alunoF}")
print(F"Total de homens acima de 18 anos: {alunoH}")


