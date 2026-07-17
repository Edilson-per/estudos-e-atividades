salario_base = 1500
comissao = 200
corretor = input("Digite seu nome:")
qntd_vendas = float(input("Digite a quantidade de vendas:"))
valor_vendas = float(input("Digite o valor das vendas:"))

salario_completo = (comissao * qntd_vendas) + (valor_vendas * (5 / 100)) + salario_base

print(f"Cálculo finalizado {corretor}, seu salário completo será: {salario_completo} ")

