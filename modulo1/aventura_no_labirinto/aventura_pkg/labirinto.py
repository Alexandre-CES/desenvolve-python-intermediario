from . import utils
from rich import print as rprint

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

    def imprimir_labirinto(self, pos):
        '''Imprime o labirinto
        
        Recebe uma tupla (x,y) que determina a posição em que o jogador está atualmente, que será imprimida no terminal junto ao labirinto'''
        
        x,y = pos
        for i in range(len(self.labirinto)):
            for j in range(len(self.labirinto[i])):
                if i == y and j == x:
                    rprint('[yellow]o', end='')
                elif self.labirinto[i][j] != '\n':
                    rprint(self.labirinto[i][j], end='')

            print()
