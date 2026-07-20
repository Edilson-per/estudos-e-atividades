import math
num = int(input("Digite um número inteiro: "))

if num % 2 == 0 :
    resultado = math.sqrt(num)
else :
    resultado = num ** 3

print(resultado)