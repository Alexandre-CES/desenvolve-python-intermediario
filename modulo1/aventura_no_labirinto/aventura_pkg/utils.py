from rich import print as rprint
from rich.panel import Panel
import argparse

def args():
    '''Adiciona os argumentos no argparser, os retornando em seguida'''

    parser = argparse.ArgumentParser(
        prog='Aventura no labirinto',
        description='tente achar a saída do labirinto se movendo com seu teclado'
    )

    parser.add_argument(
        '-d',
        '--dificuldade',
        type=int,
        default=1,
        choices=range(1,4),
        help='Determina o tamanho do labirinto'
    )

    return parser.parse_args()

def read_file(filename):
    '''Para ler o arquivo'''
    fileStr = ''
    with open(f'./assets/{filename}', 'r') as file:
        fileStr = file.read()
        return fileStr

def read_file_lines(filename):
    '''Ler o arquivo em forma de lista para acessar o x e y do labirinto'''
    fileLst = []
    with open(f'./assets/{filename}', 'r') as file:
        fileLst = file.readlines()
        return fileLst

def imprimir_instrucoes():
    '''Imprime as instruções do jogo'''

    instrucoes = read_file('instrucoes.txt')
    panel = Panel.fit(instrucoes,
        title='Instruções',
        subtitle='Se divirta!',
        border_style='bold magenta'
    )
    rprint(panel)