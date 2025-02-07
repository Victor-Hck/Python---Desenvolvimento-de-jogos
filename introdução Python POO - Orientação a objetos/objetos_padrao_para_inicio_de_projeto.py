import pygame  # Importa a biblioteca Pygame.
from obj import Obj  # Importa a classe Obj do arquivo obj.py (presume-se que exista).

class Main:  # Define a classe Main, que provavelmente representa a estrutura principal do jogo.

    def __init__(self, sizex, sizey, title):  # Método construtor da classe Main.
        # self: Refere-se à instância atual da classe Main (o objeto que está sendo criado).
        # sizex: Largura da janela do jogo.
        # sizey: Altura da janela do jogo.
        # title: Título da janela do jogo.

        self.window = pygame.display.set_mode([sizex, sizey])  # Cria a janela do jogo com as dimensões especificadas.
        self.title = pygame.display.set_caption(title)  # Define o título da janela.

        self.loop = True  # Inicializa a variável de controle do loop principal do jogo como True.
        self.list_obj = []

    def add_obj(self, item):  # Método para desenhar os elementos do jogo na tela.
        # self: Refere-se à instância atual da classe Main.
        # pass  # Por enquanto, este método não faz nada. Você precisará adicionar o código para desenhar os objetos do jogo aqui.
        self.list_obj.append(item)

    def events(self):  # Método para lidar com os eventos do jogo (ex: entrada do usuário, fechamento da janela).
        # self: Refere-se à instância atual da classe Main.
        for events in pygame.event.get():  # Itera sobre todos os eventos que ocorreram desde a última verificação.
            if events.type == pygame.QUIT:  # Verifica se o evento atual é do tipo QUIT (ou seja, o usuário clicou no botão de fechar a janela).
                self.loop = False  # Se o evento for QUIT, define a variável de controle do loop como False, o que encerrará o loop na próxima iteração.

    def update(self):  # Método principal que controla o loop do jogo.
        # self: Refere-se à instância atual da classe Main.
        while self.loop:  # Loop principal do jogo, executado enquanto self.loop for True.
            self.draw()  # Chama o método draw() para desenhar os elementos do jogo.
            self.events()  # Chama o método events() para lidar com os eventos.
            pygame.display.update()  # Atualiza a tela do jogo, tornando as mudanças visíveis.


# Cria uma instância da classe Main, definindo a largura, altura e título da janela.
game = Main(1280, 720, "Futeball Pong")

# Inicia o loop principal do jogo chamando o método update().
game.update()

# Após o loop terminar (quando o usuário fecha a janela), o programa continua a execução (se houver código depois dessa linha).
# Se não houver mais código, o programa termina.  É uma boa prática adicionar um pygame.quit() aqui, mesmo que não seja estritamente necessário nesse exemplo.
pygame.quit() # Finaliza o Pygame.