salario_minimo   = float(input("Informe o valor do salário mínimo atual (R$): "))
salario_usuario  = float(input("Informe o valor do seu salário mensal (R$): "))
qtd_salarios = salario_minimo / salario_usuario

print(f"Você recebe aproximadamente {qtd_salarios:.2f} salário(s) mínimo(s).")