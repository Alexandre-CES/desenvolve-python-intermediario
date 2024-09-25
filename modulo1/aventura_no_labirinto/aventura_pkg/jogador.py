import pynput
from rich.prompt import Prompt

class Jogador:
    '''Representa o jogador'''

    def __init__(self):
        self.nome, self.posicao, self.movimentos = '', (), 0

    def iniciar_jogador(self):
        '''Inicia o nome, posição e pontuação do personagem'''

        self.nome = Prompt.ask('Nome do personagem');print()
        self.posicao = (1, 0)
        self.movimentos = 0

    def retornar_jogador(self):
        return self.nome, self.movimentos, self.posicao

    def pontuar(self, quantidade):
        self.pontuacao += quantidade

    def mover(self, pos):
        self.movimentos += 1
        self.posicao = pos