import pygame  # Importa a biblioteca Pygame

pygame.init()  # Inicializa todos os módulos do Pygame

# Cria uma janela com resolução de 1280x720 pixels
window = pygame.display.set_mode([1280, 720])

# Define o título da janela como "Futebal Pong"
pygame.display.set_caption("Futebal Pong")

# Carrega a imagem do campo a partir do arquivo localizado em "assets\field.png"
field = pygame.image.load(r"assets\field.png")

# Carrega a imagem do jogador 1 a partir do arquivo "assets/player1.png"
player1 = pygame.image.load(r"assets\player1.png")
player1_y = 310 # Define a posição vertical inicial do jogador 1
player1_moveup = False
player1_movedown = False
# Carrega a imagem do jogador 2 a partir do arquivo "assets/player2.png"
player2 = pygame.image.load(r"assets\player2.png")

# Carrega a imagem da bola a partir do arquivo "assets/ball.png"
ball = pygame.image.load(r"assets\ball.png")

# Define as coordenadas iniciais da bola
ball_x = 617  # Posição X inicial da bola (próximo ao centro da tela)
ball_y = 337  # Posição Y inicial da bola (próximo ao centro da tela)

def move_player():
    global player1_y  # Permite modificar a variável player1_y dentro da função
    
    if player1_moveup:   # Se a flag estiver ativada
        player1_y -= 5   # Move o jogador para cima
    if player1_movedown: # Se a flag estiver ativada
        player1_y += 5   # Move o jogador para baixo
        
    #print(player1_y) # Massete para mostrar a posição do player na tela. 
    
    # Limita o movimento do jogador 1 para que ele não saia da tela
    if player1_y <= 0:
        player1_y = 0  # Impede que o jogador ultrapasse o topo da tela
        
    if player1_y >= 575:
        player1_y = 575  # Impede que o jogador ultrapasse a parte inferior da tela

# Função para movimentar a bola
def move_ball():
    global ball_x  # Usa a variável global ball_x para modificar seu valor
    global ball_y  # Usa a variável global ball_y (ainda não usada para movimento)

    ball_x += 1  # Move a bola para a direita a cada frame

# Função para desenhar os elementos na tela
def draw():
    # Desenha o campo na tela
    window.blit(field, (0, 0))  # Posição (0,0) significa que o campo cobre toda a tela

    # Desenha o jogador 1 na posição (50, 310)
    window.blit(player1, (50, player1_y))  

    # Desenha o jogador 2 na posição (1150, 310)
    window.blit(player2, (1150, 310))  

    # Desenha a bola na posição atualizada (ball_x, ball_y)
    window.blit(ball, (ball_x, ball_y))

# Variável de controle do loop principal do jogo
loop = True

while loop:  # Inicia o loop do jogo

    # Captura eventos (como teclas pressionadas ou clique para fechar)
    for events in pygame.event.get():  
        if events.type == pygame.QUIT:  # Se o evento for para fechar a janela
            loop = False  # Encerra o loop, fechando o jogo
        if events.type == pygame.KEYDOWN:  # Se uma tecla foi pressionada
            if events.key == pygame.K_w:   # Se a tecla 'W' foi pressionada
                player1_moveup = True  # Move o jogador 1 para cima
            if events.key == pygame.K_s:   # Se a tecla 'S' foi pressionada
                player1_movedown = True  # Move o jogador 1 para baixo
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:   # Se a tecla 'W' foi pressionada
                player1_moveup = False  # Move o jogador 1 para cima
            if events.key == pygame.K_s:   # Se a tecla 'S' foi pressionada
                player1_movedown = False  # Move o jogador 1 para baixo
    draw()  # Atualiza os elementos na tela
    move_ball()  # Move a bola para a direita a cada iteração
    move_player() # Move o jogador 1
    pygame.display.update()  # Atualiza a tela para refletir mudanças visuais

pygame.quit()  # Sai do Pygame corretamente ao fechar o jogo
