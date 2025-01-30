nome = "Hero"
vida = 10

gravidade = 9.8

vivo = False

nome = input("Digite o seu nome:")
vida = input("Digite o seu numero:")
print(f"nome: ", nome)
print(f"Vida: ", vida)

# > < >= <= == !=

if nome == "hero":
    print(f"O nome é Hero")
elif nome != "Hero":
    print(f"o nome é renato")
