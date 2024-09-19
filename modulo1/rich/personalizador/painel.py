from rich import print
from rich.panel import Panel

def painel_simples(text, isArquivo=False):
    content = read_text(text, isArquivo)
    panel = Panel(content, title="Painel Simples", subtitle="Exemplo de painel")
    print(panel)

def painel_com_borda(text, isArquivo=False):
    content = read_text(text, isArquivo)
    panel = Panel(content, title="Painel com Borda", border_style="bold magenta")
    print(panel)

def read_text(text, isArquivo):
    if isArquivo:
        with open(text, 'r') as f:
            return f.read()
    return text