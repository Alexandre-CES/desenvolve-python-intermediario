from . import utils

class Labirinto:
    '''Representa o labirinto'''

    labirinto = []

    def __init__(self):
        self.labirinto = []

    def criar_labirinto(self,dificuldade):
        '''Cria o labirinto que o jogador escolher'''
        
        if dificuldade == 1:
            self.labirinto = utils.read_file_lines('labirinto_facil.txt')
        elif dificuldade == 2:
            self.labirinto = utils.read_file_lines('labirinto_medio.txt')
        else:
            self.labirinto = utils.read_file_lines('labirinto_dificil.txt')

    def imprimir_labirinto(self):
        '''Imprime o labirinto'''
        for i in self.labirinto:
            print(i, end='')
        
        print()

