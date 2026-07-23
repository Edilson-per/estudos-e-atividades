estatura1 = int(input("Qual o seu estatura? "))
estatura2 = int(input("Qual o seu estatura? "))
estatura3 = int(input("Qual o seu estatura? "))

maior = estatura1

if estatura1 == estatura2 or estatura3 == estatura1 or estatura3 == estatura2:
    print("Há pelo menos 2 estaturas iguais.")
else:
    if estatura2 < maior:
        maior = estatura2
    elif estatura3 < maior:
        maior = estatura3
