nome = "Hero"
vida = 3
ataque = 3
defesa = 2
vivo = True

def main():
    print("Olá aventureiro, no que posso ajudar?")
    print()
    print("missões: ")
    print("1 - Matar goblins")
    print("2 - Coletar materiais")
    print("3 - Resgatar inocentes")
    resposta = int(input("Eu escolho: "))
    if resposta == 1:
        atacar()
    elif resposta == 2:
        coletar()
    elif resposta == 3:
        resgatar()
    else:
        print("Hhoho, Não tenho esse missão!")

def atacar():
    print("Eu vou matar goblins")

def coletar():
    print("Vou coletar meus materiais")

def resgatar():
    print("Vou resgatar os inocentes")

while True:
    main()
    sair = input("Desaja sair?")
    if sair == "sim":
        break