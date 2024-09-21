'''
    Imprime o texto em um único painel com título, subtítulo e borda colorida
'''

from rich import print
from rich.panel import Panel

def painel_simples(text, isArquivo=False):
    '''Exibe o texto em um painel simples'''
    content = read_text(text, isArquivo)
    panel = Panel.fit(content, title='Painel com Borda', subtitle='exemplo', border_style='bold magenta')
    print(panel)

def read_text(text, isArquivo):
    '''Lê texto/arquivo'''
    if isArquivo:
        with open(text, 'r') as f:
            return f.read()
    return text