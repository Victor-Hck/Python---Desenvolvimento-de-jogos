import pygame  # Importa a biblioteca Pygame.
from obj import Obj  # Importa a classe Obj do arquivo obj.py (presume-se que exista).

pygame.init()  # Inicializa todos os módulos do Pygame.  Essencial para o funcionamento correto.

window = pygame.display.set_mode([1280, 720])  # Cria a janela do jogo com largura 1280 e altura 720.
title = pygame.display.set_caption("Futeball")  # Define o título da janela como "Futeball".

# Cria instâncias da classe Obj para os elementos do jogo:
campo = Obj("assets/field.png", 0, 0)  # Cria o objeto campo, carregando a imagem "assets/field.png" e posicionando-o em (0, 0).
campo.draw(window)  # Desenha o campo na janela.

player1 = Obj("assets/player1.png", 50, 300)  # Cria o objeto player1, carregando a imagem "assets/player1.png" e posicionando-o em (50, 300).
player1.draw(window)  # Desenha o player1 na janela.

player2 = Obj("assets/player2.png", 1000, 300)  # Cria o objeto player2, carregando a imagem "assets/player2.png" e posicionando-o em (1000, 300).
player2.draw(window)  # Desenha o player2 na janela.

loop = True  # Inicializa a variável de controle do loop principal do jogo como True.
while loop:  # Inicia o loop principal do jogo.
    for events in pygame.event.get():  # Itera sobre todos os eventos que ocorreram desde a última verificação.
        if events.type == pygame.QUIT:  # Verifica se o evento atual é do tipo QUIT (ou seja, o usuário clicou no botão de fechar a janela).
            loop = False  # Se o evento for QUIT, define a variável de controle do loop como False, o que encerrará o loop na próxima iteração.

    pygame.display.update()  # Atualiza a tela do jogo, redesenhando todos os elementos.  Importante para exibir as mudanças.

pygame.quit()  # Finaliza o Pygame, liberando os recursos utilizados.  Essencial para evitar problemas e travamentos.
