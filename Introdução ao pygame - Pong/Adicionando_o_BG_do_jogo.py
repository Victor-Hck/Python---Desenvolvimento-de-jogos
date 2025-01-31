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

# Variável de controle do loop principal do jogo
loop = True

while loop:  # Inicia o loop do jogo

    # Captura eventos (como teclas pressionadas ou clique para fechar)
    for events in pygame.event.get():  
        if events.type == pygame.QUIT:  # Se o evento for para fechar a janela
            loop = False  # Encerra o loop, fechando o jogo

    pygame.display.update()  # Atualiza a tela para refletir mudanças visuais