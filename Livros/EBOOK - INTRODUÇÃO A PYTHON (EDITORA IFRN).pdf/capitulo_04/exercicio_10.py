aluno_reprovado = 0
aluno_prova_final = 0
aluno_aprovado = 0

for i in range (5) :
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    if media < 2 :
        aluno_reprovado += 1
    elif 2 <= media < 6 :
        aluno_prova_final += 1
    if media >= 6 :
        aluno_aprovado += 1

percentual_final = (aluno_prova_final / 5) * 100

print(f"Alunos na prova  final: {percentual_final}")