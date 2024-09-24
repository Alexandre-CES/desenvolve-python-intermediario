import pynput
from rich.prompt import Prompt

class Jogador:
    '''Representa o jogador'''

    nome = ''
    posicao = ()
    pontuacao = 0

    def __init__(self):
        self.nome, self.posicao, self.pontuacao = '', (), 0

    def iniciar_jogador(self):
        '''Inicia o nome, posição e pontuação do personagem'''

        self.nome = Prompt.ask('Nome do personagem');print()
        self.posicao = (1, 0)
        self.pontuacao = 0

    def retornar_jogador(self):
        return self.nome, self.pontuacao, self.posicao

    def pontuar(self, quantidade):
        self.pontuacao += quantidade

    def mover():
        pass