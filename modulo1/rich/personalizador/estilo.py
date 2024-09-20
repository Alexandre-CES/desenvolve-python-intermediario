from rich import print as rprint  
from itertools import cycle

def estilo_negrito(text, isArquivo=False):
    '''Deixa todo o texto em negrito'''
    content = read_text(text, isArquivo)
    rprint(f"[bold]{content}[/bold]")

def estilo_rainbow(text, isArquivo=False):
    '''Faz cada linha ter uma cor diferente
    
    utiliza a função/classe cycle() da biblioteca -itertools- para iterar na lista, de forma que a iteração volte na posição 0 após o último item.    

    Com isso, é aplicado a cor resultante de cada iteração na linha correspondente'''

    content = read_text_lines(text, isArquivo)
    cores = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    ciclo_cores = cycle(cores)

    for line in content:
        cor_atual = next(ciclo_cores)
        rprint(f'[{cor_atual}]{line}')
    
def read_text_lines(text, isArquivo):
    '''lê separadamente as linhas do texto/arquivo'''
    if isArquivo:
        with open(text, 'r') as file:
            return file.readlines()
    return text.splitlines()

def read_text(text, isArquivo):
    '''Lê texto/arquivo'''
    if isArquivo:
        with open(text, 'r') as f:
            return f.read()
    return text