import math

num1 = float(input("Digite o primeiro número inteiro e positivo: "))
num2 = float(input("Digite o segundo número inteiro e positivo: "))

cubo_num2 = num2 ** 3

media_geometrica = math.sqrt(num1 * num2)

print(f"Resultado do cubo do segundo número {cubo_num2} seguindo resultado da media geométrica do dois valores {media_geometrica:.3f}")