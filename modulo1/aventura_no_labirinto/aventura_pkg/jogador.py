from rich.prompt import Prompt

class Jogador:
    '''Representa o jogador'''

    def __init__(self):
        self.nome, self.posicao, self.movimentos = '', (), 0

    def iniciar_jogador(self, nome):
        '''Inicia o nome, posição e pontuação do personagem'''

        self.nome = nome
        self.posicao = (1, 0)
        self.movimentos = 0

    def retornar_jogador(self):
        '''Retorna informações do jogador'''
        return self.nome, self.movimentos, self.posicao

    def mover(self, pos):
        '''define nova posição do jogador'''
        self.movimentos += 1
        self.posicao = pos