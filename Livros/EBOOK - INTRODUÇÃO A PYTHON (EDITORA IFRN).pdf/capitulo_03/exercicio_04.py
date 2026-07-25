user1 = 'Procopio'
key1 = 12345
user2 = 'Paiva'
key2 = 54321


validaUser = input("Digite o usuário: ")
validaKey = int(input("Digite a senha: "))

if validaUser == user1 and validaKey == key1:
    print(f"Bem vindo {user1}")
elif validaUser == user2 and validaKey == key2:
    print(f"Bem vindo {user2}")
else:
    print("Usuário ou senha incorreto(s)")