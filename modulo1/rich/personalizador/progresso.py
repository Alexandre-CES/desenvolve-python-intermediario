from rich.progress import Progress
from time import sleep
from rich import print

def barra_progresso(text, isArquivo=False):
    content = read_text(text, isArquivo)
    with Progress() as progress:
        task = progress.add_task(f'[green]processando...', total=100)
        while not progress.finished:
            progress.update(task, advance=1)
            sleep(0.02)
    print(content)

def barra_progresso_tasks(text, isArquivo=False):
    content = read_text(text, isArquivo)
    total_lines = len(content)
    with Progress() as progress:
        task1 = progress.add_task("[red]Downloading...", total=total_lines)
        task2 = progress.add_task("[green]Processing...", total=total_lines)
        task3 = progress.add_task("[cyan]Cooking...", total=total_lines)

        for i, line in enumerate(content):
            progress.update(task1, advance=2)
            progress.update(task2, advance=1)
            progress.update(task3, advance=1.5)
            sleep(0.1)
            print(line)
        
        progress.stop()

            

def read_text(text, isArquivo):
    if isArquivo:
        with open(text, 'r') as file:
            return file.readlines()
    return text.splitlines()
