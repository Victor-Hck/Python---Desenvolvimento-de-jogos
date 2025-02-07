from objetos_padrao_para_inicio_de_projeto import Main
from obj import Obj

class Game:
    
    def __init__(self):
        self.tela = Main(1280, 720, "Pong Futeball")
        
        self.bg = Obj("assets/field.png", 0, 0)
        self.tela.add_obj(self.bg)  # Adicionando o fundo corretamente

        self.player1 = Obj("assets/player1.png", 0, 0)
        self.tela.add_obj(self.player1)  # Agora player1 já está definido antes de ser usado

Game().tela.update()