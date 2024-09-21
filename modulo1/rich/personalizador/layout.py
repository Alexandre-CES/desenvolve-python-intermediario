'''
    Imprime o conteúdo dividido em partes

    Está dividido em três funções, uma para ler o arquivo, outra para dividi-lo, outra para imprimi-lo
'''

from rich.layout import Layout
from rich.console import Console

def print_layout(text, isArquivo=False):
    """Divide o conteúdo em três partes e o exibe nas áreas do layout."""
    layout = Layout()

    layout.split_column(
        Layout(name="upper"),
        Layout(name="lower")
    )

    layout["lower"].split_row(
        Layout(name="left"),
        Layout(name="right"),
    )

    content = read_text(text, isArquivo)

    partes = dividir_texto_em_partes(content, 3)

    upper_content = '\n'.join(partes[0])
    layout["upper"].update(f"[bold red]Upper Layout[/bold red]\n{upper_content}")
    
    left_content = '\n'.join(partes[1])
    layout["left"].update(f"[green]Left side[/green]\n{left_content}")
    
    right_content = '\n'.join(partes[2])
    layout["right"].update(f"[blue]Right side[/blue]\n{right_content}")

    console = Console()
    console.print(layout)

def dividir_texto_em_partes(texto, num_partes):
    """Divide o texto em um número especificado de partes."""
    tamanho = len(texto)
    parte_tamanho = tamanho // num_partes

    partes = []
    for i in range(num_partes):
        inicio = i * parte_tamanho
        if i == num_partes - 1:
            partes.append(texto[inicio:])
        else:
            partes.append(texto[inicio:inicio + parte_tamanho])
    
    return partes

def read_text(text, isArquivo):
    '''Lê texto/arquivo'''
    if isArquivo:
        with open(text, 'r') as f:
            return f.readlines()
    return text