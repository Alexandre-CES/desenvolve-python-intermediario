from rich import print
from rich.layout import Layout

def print_layout(text, isArquivo=False):

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
    layout["upper"].update(f"[bold red]Upper Layout[/bold red]\n{content}")
    layout["left"].update("[green]Left side[/green]")
    layout["right"].update("[blue]Right side[/blue]")

    print(layout)

def read_text(text, isArquivo):
    if isArquivo:
        with open(text, 'r') as f:
            return f.read()
    return text