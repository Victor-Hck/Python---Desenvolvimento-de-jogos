import pygame  # Importa a biblioteca Pygame

pygame.init()  # Inicializa todos os módulos do Pygame

# Cria uma janela com resolução de 1280x720 pixels
window = pygame.display.set_mode([1280, 720])

# Define o título da janela como "Futebal Pong"
title = pygame.display.set_caption("Futebal Pong")

# Carrega a imagem do campo a partir do arquivo localizado em "assets\field.png"
field = pygame.image.load(r"assets\field.png")

# Desenha a imagem do campo na janela do jogo
window.blit(field, (0, 0)) # Proporção da imagem na tela

# Carrega a imagem do jogador 1 a partir do arquivo "assets/player1.png"
player1 = pygame.image.load(r"assets\player1.png")

# Desenha o jogador 1 na posição (50, 310)
# Isso significa que ele será colocado a 50 pixels da borda esquerda e 310 pixels do topo
window.blit(player1, (50, 310))  

# Carrega a imagem do jogador 2 a partir do arquivo "assets/player2.png"
player2 = pygame.image.load(r"assets\player2.png")

# Desenha o jogador 2 na posição (1150, 310)
# Ele será posicionado mais à direita, perto da borda direita da tela
window.blit(player2, (1150, 310))  

# Carrega a imagem da bola a partir do arquivo "assets/ball.png"
ball = pygame.image.load(r"assets\ball.png")

# Desenha a bola na posição (620, 330), aproximadamente no centro da tela
window.blit(ball, (620, 330)) 

# Variável de controle do loop principal do jogo
loop = True

while loop:  # Inicia o loop do jogo

    # Captura eventos (como teclas pressionadas ou clique para fechar)
    for events in pygame.event.get():  
        if events.type == pygame.QUIT:  # Se o evento for para fechar a janela
            loop = False  # Encerra o loop, fechando o jogo

    pygame.display.update()  # Atualiza a tela para refletir mudanças visuais