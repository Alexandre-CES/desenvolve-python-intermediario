import argparse
from rich import print as rprint
from rich.panel import Panel
from rich.prompt import Prompt

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

def tela_inicial():
    '''Menu inicial'''
    while True:
        rprint('\nAventura no labirinto\n')
        rprint('[1]Jogar - [2]Instruções')
        opt = Prompt.ask('Escolha',choices=['1','2'], show_choices=True);print()

        match opt:
            case '1':
                return
            case '2':
                imprimir_instrucoes()
            case outro:
                rprint(f'{outro} não é uma opção válida! ')

def finalizar_jogo(jogador, dificuldade):
    nome, movimentos, posicao = jogador.retornar_jogador()

    panel = Panel.fit(
        f'O jogador [purple]{nome}[/purple] finalizou o modo [purple]{dificuldade}[/purple] com o total de [purple]{movimentos}[/purple] movimentos na posição [purple]{posicao}[/purple]',
        title='Parabéns!',
        subtitle='As vezes é necessário dar um passo para trás para dar dois para frente',
        border_style='yellow'
    )
    rprint(panel)

def read_file(filename):
    '''Para ler o arquivo'''
    fileStr = ''
    with open(f'./assets/{filename}', 'r', encoding='utf-8') as file:
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
    panel = Panel.fit(
        instrucoes,
        title='Instruções',
        subtitle='Se divirta!',
        border_style='bold magenta'
    )
    rprint(panel)
    input('(Enter)Retornar...');print()