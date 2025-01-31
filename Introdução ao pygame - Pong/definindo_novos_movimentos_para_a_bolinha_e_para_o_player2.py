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
player1_y = 310  # Define a posição vertical inicial do jogador 1

# Variáveis de controle para movimentação do jogador 1
player1_moveup = False   # Indica se o jogador 1 está se movendo para cima
player1_movedown = False # Indica se o jogador 1 está se movendo para baixo

# Carrega a imagem do jogador 2 a partir do arquivo "assets/player2.png"
player2 = pygame.image.load(r"assets/player2.png")
player2_y = 310  # Define a posição vertical inicial do jogador 2

# Carrega a imagem da bola a partir do arquivo "assets/ball.png"
ball = pygame.image.load(r"assets\ball.png")

# Define as coordenadas iniciais da bola
ball_x = 617  # Posição X inicial da bola (próximo ao centro da tela)
ball_y = 337  # Posição Y inicial da bola (próximo ao centro da tela)
ball_dir = -5  # Define a direção inicial da bola (movendo-se para a esquerda)
ball_dir_y = 1  # Define a direção inicial da bola no eixo Y (movendo-se para baixo)

# Função para movimentar o jogador 1
def move_player():
    global player1_y  # Permite modificar a variável player1_y dentro da função
    
    # Se a flag de movimento estiver ativada, move o jogador para cima ou para baixo
    if player1_moveup:
        player1_y -= 5  # Move o jogador para cima
    
    if player1_movedown:
        player1_y += 5  # Move o jogador para baixo

    # Limita o movimento do jogador 1 para que ele não saia da tela
    if player1_y <= 0:
        player1_y = 0  # Impede que o jogador ultrapasse o topo da tela
    
    if player1_y >= 575:
        player1_y = 575  # Impede que o jogador ultrapasse a parte inferior da tela

def move_player2():
    global player2_y
    player2_y = ball_y
# Função para movimentar a bola
def move_ball():
    global ball_x  # Usa a variável global ball_x para modificar seu valor
    global ball_y  # Usa a variável global ball_y (ainda não usada para movimento)
    global ball_dir  # Usa a variável global ball_dir para alterar a direção da bola
    global ball_dir_y  # Usa a variável global ball_dir_y para alterar a direção da bola
    
    ball_x += ball_dir  # Move a bola na direção atual
    ball_y += ball_dir_y  # Move a bola na direção atual (vertical)
    
    # Verifica colisão da bola com o jogador 1
    if ball_x < 120:  # Se a bola atingir a área do jogador 1
        if player1_y < ball_y + 23:  # Verifica se a bola está dentro da altura do jogador 1
            if player1_y + 146 > ball_y:  # Verifica se a bola ainda está dentro do jogador
                ball_dir *= -1  # Inverte a direção da bola (rebate)

    # Verifica colisão da bola com o jogador 2
    if ball_x > 1100:  # Se a bola atingir a área do jogador 2
        if player2_y < ball_y + 23:  # Verifica se a parte superior da bola está abaixo da parte inferior do jogador 2
            if player2_y + 146 > ball_y:  # Verifica se a parte inferior da bola está acima da parte superior do jogador 2
                ball_dir *= -1  # Inverte a direção da bola (rebate)

    # Verifica colisão da bola com as bordas superior e inferior da tela
    if ball_y > 685:  # Se a bola atingir a borda inferior
        ball_dir_y *= -1  # Inverte a direção da bola (rebate)
    elif ball_y <= 0:  # Se a bola atingir a borda superior
        ball_dir_y *= -1  # Inverte a direção da bola (rebate)

# Função para desenhar os elementos na tela
def draw():
    # Desenha o campo na tela
    window.blit(field, (0, 0))  # Posição (0,0) significa que o campo cobre toda a tela

    # Desenha o jogador 1 na posição (50, player1_y)
    window.blit(player1, (50, player1_y))  

    # Desenha o jogador 2 na posição fixa (1150, 310)
    window.blit(player2, (1150, player2_y))  

    # Desenha a bola na posição atualizada (ball_x, ball_y)
    window.blit(ball, (ball_x, ball_y))

# Variável de controle do loop principal do jogo
loop = True

while loop:  # Inicia o loop do jogo

    # Captura eventos (como teclas pressionadas ou clique para fechar)
    for events in pygame.event.get():  
        if events.type == pygame.QUIT:  # Se o evento for para fechar a janela
            loop = False  # Encerra o loop, fechando o jogo
        
        # Verifica se alguma tecla foi pressionada
        if events.type == pygame.KEYDOWN:  
            if events.key == pygame.K_w:   # Se a tecla 'W' foi pressionada
                player1_moveup = True  # Ativa o movimento para cima
            if events.key == pygame.K_s:   # Se a tecla 'S' foi pressionada
                player1_movedown = True  # Ativa o movimento para baixo
        
        # Verifica se alguma tecla foi solta
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:   # Se a tecla 'W' foi solta
                player1_moveup = False  # Para o movimento para cima
            if events.key == pygame.K_s:   # Se a tecla 'S' foi solta
                player1_movedown = False  # Para o movimento para baixo

    draw()          # Atualiza os elementos na tela
    move_ball()     # Move a bola e verifica colisões
    move_player()   # Move o jogador 1 conforme as teclas pressionadas
    move_player2()  # Move o jogador 2 (IA)
    pygame.display.update()  # Atualiza a tela para refletir mudanças visuais

pygame.quit()  # Sai do Pygame corretamente ao fechar o jogo
