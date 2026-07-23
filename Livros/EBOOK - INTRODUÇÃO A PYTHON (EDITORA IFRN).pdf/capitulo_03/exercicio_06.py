sobreNome1 = "Pinheiro"
sobreNome2 = "Araújo"
sobreNome3 = "Bonner"
sobreNome4 = "Vasconcelos"

escolhaSobreNome = input("Digite o nome do escolhido: ")

if escolhaSobreNome == sobreNome1 or escolhaSobreNome == sobreNome2:
    print(f"O programa apresentador por: {escolhaSobreNome}, se chama Bom dia Nação ")
elif escolhaSobreNome == sobreNome3 or escolhaSobreNome == sobreNome4:
    print(f"O programa apresentador por: {escolhaSobreNome}, se chama Jornal Brasileiro ")
else :
    print("Nome desconhecido ou não encontrado")
