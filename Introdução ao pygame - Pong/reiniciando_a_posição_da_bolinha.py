import pygame  # Importa a biblioteca Pygame

pygame.init()  # Inicializa todos os módulos do Pygame

# Cria uma janela com resolução de 1280x720 pixels
window = pygame.display.set_mode([1280, 720])

# Define o título da janela como "Futebal Pong"
pygame.display.set_caption("Futebal Pong")

win = pygame.image.load("assets/win.png")  # Carrega a imagem de vitória para ser exibida quando um jogador vence.

score1 = 0  # Inicializa o placar do jogador 1
score1_img = pygame.image.load(r"assets\score\0.png")  # Carrega a imagem do placar
score2 = 8  # Inicializa o placar do jogador 2
score2_img = pygame.image.load(r"assets\score\0.png")  # Carrega a imagem do placar

field = pygame.image.load(r"assets\field.png")  # Carrega a imagem do campo

player1 = pygame.image.load(r"assets\player1.png")  # Carrega a imagem do jogador 1
player1_y = 310  # Define a posição vertical inicial do jogador 1

player1_moveup = False  # Indica se o jogador 1 está se movendo para cima
player1_movedown = False  # Indica se o jogador 1 está se movendo para baixo

player2 = pygame.image.load(r"assets/player2.png")  # Carrega a imagem do jogador 2
player2_y = 310  # Define a posição vertical inicial do jogador 2

ball = pygame.image.load(r"assets\ball.png")  # Carrega a imagem da bola

ball_x = 617  # Define a posição inicial X da bola
ball_y = 337  # Define a posição inicial Y da bola
ball_dir = -5  # Define a direção horizontal inicial da bola
ball_dir_y = 1  # Define a direção vertical inicial da bola

# Função para movimentar o jogador 1
def move_player():
    global player1_y  # Permite modificar a variável player1_y dentro da função
    
    if player1_moveup:
        player1_y -= 5  # Move o jogador para cima
    
    if player1_movedown:
        player1_y += 5  # Move o jogador para baixo

    # Limita o movimento do jogador 1 para que ele não saia da tela
    if player1_y <= 0:
        player1_y = 0  # Impede que o jogador ultrapasse o topo da tela
    
    if player1_y >= 575:
        player1_y = 575  # Impede que o jogador ultrapasse a parte inferior da tela

# Função para movimentar o jogador 2 (IA simples)
def move_player2():
    global player2_y
    player2_y = ball_y  # Faz o jogador 2 seguir a bola

# Função para movimentar a bola
def move_ball():
    global ball_x, ball_y, ball_dir, ball_dir_y, score1, score2, score1_img, score2_img
    
    ball_x += ball_dir  # Move a bola na direção horizontal
    ball_y += ball_dir_y  # Move a bola na direção vertical
    
    # Verifica colisão da bola com o jogador 1
    if ball_x < 120:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_dir *= -1  # Inverte a direção da bola

    # Verifica colisão da bola com o jogador 2
    if ball_x > 1100:
        if player2_y < ball_y + 23:
            if player2_y + 146 > ball_y:
                ball_dir *= -1  # Inverte a direção da bola

    # Verifica colisão da bola com as bordas superior e inferior
    if ball_y > 685 or ball_y <= 0:
        ball_dir_y *= -1  # Inverte a direção vertical da bola para evitar que ela continue se movendo na mesma trajetória.

    # Verifica se a bola saiu pela esquerda (ponto para o jogador 2)
    if ball_x < -50:
        ball_x, ball_y = 617, 337  # Reseta a posição da bola para o centro
        ball_dir_y *= -1  # Inverte a direção vertical da bola
        ball_dir *= -1  # Inverte a direção horizontal da bola
        score2 += 1  # Adiciona um ponto ao jogador 2
        score2_img = pygame.image.load("assets/score/" + str(score2) + ".png")  # Atualiza a imagem do placar
    # Verifica se a bola saiu pela direita (ponto para o jogador 1)
    elif ball_x > 1320:
        ball_x, ball_y = 617, 337  # Reseta a posição da bola para o centro
        ball_dir_y *= -1  # Inverte a direção vertical da bola
        ball_dir *= -1  # Inverte a direção horizontal da bola
        score1 += 1  # Adiciona um ponto ao jogador 1
        score1_img = pygame.image.load("assets/score/" + str(score1) + ".png")  # Atualiza a imagem do placar

# Função para desenhar os elementos na tela
def draw():
    if score1 or score2 < 9:
        window.blit(field, (0, 0))  # Desenha o campo
        window.blit(player1, (50, player1_y))  # Desenha o jogador 1
        window.blit(player2, (1150, player2_y))  # Desenha o jogador 2
        window.blit(ball, (ball_x, ball_y))  # Desenha a bola
        window.blit(score1_img, (500, 50))  # Exibe a pontuação do jogador 1
        window.blit(score2_img, (710,50))  # Exibe a pontuação do jogador 2
        move_ball()  # Move a bola e verifica colisões
        move_player()  # Move o jogador 1
        move_player2()  # Move o jogador 2 (IA)
    else:
        window.blit(win, (300, 330))  # Exibe a tela de vitória

loop = True  # Variável de controle do loop principal do jogo

while loop:
    for events in pygame.event.get():  # Captura eventos
        if events.type == pygame.QUIT:
            loop = False  # Sai do loop e fecha o jogo
        
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                player1_moveup = True
            if events.key == pygame.K_s:
                player1_movedown = True
        
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player1_moveup = False
            if events.key == pygame.K_s:
                player1_movedown = False

    draw()  # Atualiza os elementos na tela
    pygame.display.update()  # Atualiza a tela para refletir mudanças visuais

pygame.quit()  # Sai do Pygame corretamente ao fechar o jogo
