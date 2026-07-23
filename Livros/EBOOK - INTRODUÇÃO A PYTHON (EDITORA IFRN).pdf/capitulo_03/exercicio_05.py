cargo1 = "Programador de Sistemas"
cargo2 = "Analista de Sistemas"
cargo3 = "Analista de Banco de dados"

cargoUser = input("Digite seu cargo na empresa: ")
salarioUser = float(input("Digite seu salário: "))

if cargoUser == cargo1:
    acrescimoSalario = salarioUser * 0.3
    salarioTotal = salarioUser + acrescimoSalario
    print(f"Seu salário atual será de {salarioTotal}")
elif cargoUser == cargo2:
    acrescimoSalario = salarioUser * 0.2
    salarioTotal = salarioUser + acrescimoSalario
    print(f"Seu salário atual será de {salarioTotal}")
elif cargoUser == cargo3:
    acrescimoSalario = salarioUser * 0.15
    salarioTotal = salarioUser + acrescimoSalario
    print(f"Seu salário atual será de {salarioTotal}")
else :
    print("Seu cargo é inválido")

