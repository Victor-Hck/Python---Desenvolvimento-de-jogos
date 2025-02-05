import pygame  # Importa a biblioteca Pygame.

class Obj:  # Define a classe Obj, que representa um objeto do jogo (ex: jogador, inimigo, item, etc.).

    def __init__(self, image, x, y):  # Método construtor da classe Obj.  É chamado quando um novo objeto Obj é criado.
        # self: Refere-se à instância atual do objeto (o objeto que está sendo criado).
        # image: O caminho para o arquivo de imagem do objeto.
        # x: A coordenada x inicial do objeto.
        # y: A coordenada y inicial do objeto.

        self.image = pygame.image.load(image)  # Carrega a imagem do objeto usando pygame.image.load().
        self.rect = self.image.get_rect()  # Obtém o retângulo (rect) da imagem. O rect é usado para controlar a posição e tamanho do objeto.
        # O rect é um objeto do Pygame que armazena informações sobre um retângulo:
        #   - self.rect[0]: Coordenada x do canto superior esquerdo do retângulo.
        #   - self.rect[1]: Coordenada y do canto superior esquerdo do retângulo.
        #   - self.rect[2]: Largura do retângulo.
        #   - self.rect[3]: Altura do retângulo.

        self.rect[0] = x  # Define a coordenada x do retângulo para o valor passado como argumento (x).
        self.rect[1] = y  # Define a coordenada y do retângulo para o valor passado como argumento (y).
        # self.rect[2] =  # Tamanho em x (largura).  Não está sendo definido aqui, então usará o tamanho da imagem carregada.
        # self.rect[3] =  # Tamanho em y (altura).  Não está sendo definido aqui, então usará o tamanho da imagem carregada.

    def draw(self, window):  # Método para desenhar o objeto na tela.
        # self: Refere-se à instância atual do objeto.
        # window: A janela do jogo onde o objeto será desenhado.

        window.blit(self.image, (self.rect[0], self.rect[1]))  # Desenha a imagem do objeto na janela na posição especificada por self.rect[0] e self.rect[1].
        # blit() é uma função do Pygame que desenha uma imagem em outra superfície (no caso, a janela do jogo).
        # O primeiro argumento é a imagem a ser desenhada.
        # O segundo argumento é uma tupla que especifica a posição (x, y) onde a imagem será desenhada.