import sys
from . import utils
from rich import print as rprint

class Labirinto:
    '''Representa o labirinto'''

    def __init__(self):
        self.labirinto = []
        self.posicao_final = ()

    def criar_labirinto(self,dificuldade):
        '''Cria o labirinto que o jogador escolher
        
        a {dificuldade} vem do argumento de execução (-d, --dificuldade). A única diferença real é o tamanho dos labirintos'''
        
        match dificuldade:
            case 1:
                self.labirinto = utils.read_file_lines('labirinto_facil.txt')
                self.posicao_final = (9,8)
            case 2:
                self.labirinto = utils.read_file_lines('labirinto_medio.txt')
                self.posicao_final = (13,12)
            case 3:
                self.labirinto = utils.read_file_lines('labirinto_dificil.txt')
                self.posicao_final = (21,12)
            case outro:
                print('ops... Algo de errado não está certo')
                print(f'Opção {outro} é inválida')
                sys.exit(1)

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
