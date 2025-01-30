nome = "H"
vida = 10
gravidade = 9.8
vivo = True

def ataque(x):
    print("dano: ", x)

def pulo():
    print("pular")

def defesa():
    print("Defender")

# Aqui nós chamamos os nossos parametros dentro da função
def criar_plataformas():
    print("Criou uma plataforma")

for n in range(10):
    criar_plataformas()