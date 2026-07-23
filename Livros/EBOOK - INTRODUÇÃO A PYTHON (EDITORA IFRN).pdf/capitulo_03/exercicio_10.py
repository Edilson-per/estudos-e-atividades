peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"IMC: {imc:.1f} - Abaixo do peso")
elif imc < 25:
    print(f"IMC: {imc:.1f} - Peso normal")
elif imc < 30:
    print(f"IMC: {imc:.1f} - Sobrepeso")
elif imc < 35:
    print(f"IMC: {imc:.1f} - Obesidade grau 1")
elif imc < 40:
    print(f"IMC: {imc:.1f} - Obesidade grau 2")
else:
    print(f"IMC: {imc:.1f} - Obesidade grau 3")