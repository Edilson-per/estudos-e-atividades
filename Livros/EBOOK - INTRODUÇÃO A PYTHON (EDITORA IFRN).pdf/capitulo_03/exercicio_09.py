hubPagamento = """=============================================
       TABELA DE OPÇÕES DE PAGAMENTO       
=============================================
CÓD.   | FORMA DE PAGAMENTO   | DESCONTO  
---------------------------------------------
[1]    | À vista / Pix        | 15% OFF
[2]    | Débito               | 10% OFF
[3]    | Crédito à vista      | 5% OFF
============================================="""

print(hubPagamento)
valorDeVendas = float(input("Valor em vendas? "))
tipoPagamento = int(input("Tipo de Pagamento? "))

if tipoPagamento == 1:
    resultado = valorDeVendas - (valorDeVendas * 0.15)
elif tipoPagamento == 2:
    resultado = valorDeVendas - (valorDeVendas * 0.10)
elif tipoPagamento == 3:
    resultado = valorDeVendas - (valorDeVendas * 0.05)
else:
    resultado = valorDeVendas
    print("Nenhum desconto aplicado.")

print(f"O valor total da venda deu: {resultado:.2f}")



