from rich.progress import Progress
from time import sleep
from rich import print

def barra_progresso(text, isArquivo=False):
    '''Carrega uma barra (processando...) antes de mostrar o conteúdo'''
    content = read_text(text, isArquivo)
    with Progress() as progress:
        task = progress.add_task(f'[green]processando...', total=100)
        while not progress.finished:
            progress.update(task, advance=1)
            sleep(0.02)
    print(content)

def barra_progresso_tasks(text, isArquivo=False):
    '''Carrega três barras enquanto o texto está sendo enviado
    
    Fiz o download acabar primeiro, seguido por cooking e processing. Quando a última finalizar, o texto tambeḿ será totalmente enviado.

    Como o total da barra tem o mesmo tamanho do texto, é certo que finalizarão ao mesmo tempo.'''

    content = read_text(text, isArquivo)
    total_lines = len(content) #Pegar quantidade de linhas

    with Progress() as progress:
        
        #as tasks terão o total igual ao do texto
        task1 = progress.add_task("[red]Downloading...", total=total_lines)
        task2 = progress.add_task("[green]Processing...", total=total_lines)
        task3 = progress.add_task("[cyan]Cooking...", total=total_lines)

        #printar cada linha separadamente, enchendo um pouco de cada barra no processo
        for i, line in enumerate(content):
            progress.update(task1, advance=2)
            progress.update(task2, advance=1)
            progress.update(task3, advance=1.5)
            sleep(0.1)
            print(line)
        
        progress.stop()

def read_text(text, isArquivo):
    '''lê separadamente as linhas do texto/arquivo'''
    if isArquivo:
        with open(text, 'r') as file:
            return file.readlines()
    return text.splitlines()
