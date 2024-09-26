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
        '-n',
        '--nome',
        default='Jogador',
        help='Escolher o nome do jogador'
    )

    parser.add_argument(
        '-d',
        '--dificuldade',
        type=int,
        default=1,
        choices=range(1,4),
        help='Determina o tamanho do labirinto'
    )

    parser.add_argument(
        '-c1',
        '--primary_color',
        default='yellow',
        help='Escolhe a cor primário'
    )

    parser.add_argument(
        '-c2',
        '--secundary_color',
        help='Escolhe a cor secundária'
    )

    parser.add_argument(
        '-s',
        '--sound',
        action='store_true',
        help='Ativa música no jogo'
    )

    return parser.parse_args()

def tela_inicial():
    '''Menu inicial'''

    arg = args()
    while True:
        rprint(f'\n[{arg.primary_color}]Aventura no labirinto[/{arg.primary_color}]\n')
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
    '''Mostra informações do jogador em uma tela de finalização'''
    
    arg = args()
    nome, movimentos, posicao = jogador.retornar_jogador()

    panel = Panel.fit(
        f'O jogador [{arg.secundary_color}]{nome}[/{arg.secundary_color}] finalizou o modo [{arg.secundary_color}]{dificuldade}[/{arg.secundary_color}] com o total de [{arg.secundary_color}]{movimentos}[/{arg.secundary_color}] movimentos na posição [{arg.secundary_color}]{posicao}[/{arg.secundary_color}]',
        title='Parabéns!',
        subtitle='As vezes é necessário dar um passo para trás para dar dois para frente',
        border_style=arg.primary_color
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