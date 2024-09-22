def criar_labirito():
    opt = choose(1,2)

def choose(min, max):
    ''' Funçaõ para escolher uma opção no menu

    Recebe um valor mínimo e máximo, e pedirá um input enquanto não receber um número válido. Utilizei um try - except ValueError no caso de não escolherem um número
    '''
    opt = 0
    while True:
        try:
            opt = int(input('Escolha uma opção: '))
            if opt >= min and opt <= max:
                break
        except ValueError:
            print('Opção inválida, tente novamente!')
    return opt


def read_file(filename):
    labirinto = ''
    with open(f'../assets/{filename}', 'r') as file:
        labirinto = file.read()
        return labirinto