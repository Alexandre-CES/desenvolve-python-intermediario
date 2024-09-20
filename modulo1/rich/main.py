import personalizador as ps
import argparse
import sys

es = ps.estilo
la = ps.layout
pa = ps.painel
pr = ps.progresso

def Main():

    parser = argparse.ArgumentParser(
        description="Programa para imprimir texto ou conteúdo de arquivo usando Rich com opções de módulos e funções personalizadas.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    #argumentos
    parser.add_argument(
        'filename',
        help='texto ou nome de arquivo de deseja imprimir'
    )
    parser.add_argument(
        '-a',
        '--arquivo',
        action='store_true',
        help='Ativada quando o argumento é o caminho para um arquivo.'
    )
    parser.add_argument(
        '-m',
        '--modulo',
        help='''    Escolhe o módulo que a pessoa quer acessar.
    Módulos disponíveis: [1]layout, [2]painel, [3]progresso, [4]estilo.'''
    )
    parser.add_argument(
        '-f',
        '--funcao',
        help='''    Escolhe a função do módulo que quer acessar (por nome ou por id).
    [1]layout -> [1]print_layout
    [2]painel -> [1]painel_simples, [2]painel_com_borda
    [3]progresso -> [1]barra_progresso, [2]barra_progresso_tasks'''
    )

    args = parser.parse_args()

    if args.funcao and not args.modulo:
        print("Erro: Você deve especificar um módulo com a opção -m antes de usar -f.")
        sys.exit(1)

    if args.modulo == 'layout' or args.modulo == '1':
        la.print_layout(args.filename, args.arquivo)

    elif args.modulo == 'painel' or args.modulo == '2':
        if args.funcao == 'painel_simples' or args.funcao == '1':
            pa.painel_simples(args.filename, args.arquivo)
        elif args.funcao == 'painel_com_borda' or args.funcao == '2':
            pa.painel_com_borda(args.filename, args.arquivo)
        else:
            print("Erro: Função não reconhecida no módulo painel.")
            sys.exit(1)

    elif args.modulo == 'progresso' or args.modulo == '3':
        if args.funcao == 'barra_progresso' or args.funcao == '1':
            pr.barra_progresso(args.filename, args.arquivo)
        elif args.funcao == 'barra_progresso_tasks' or args.funcao == '2':
            pr.barra_progresso_tasks(args.filename, args.arquivo)
        else:
            print("Erro: Função não reconhecida no módulo progresso.")
            sys.exit(1)

    elif args.modulo == 'estilo' or args.modulo == '4':
        if args.funcao == 'estilo_negrito' or args.funcao == '1':
            es.estilo_negrito(args.filename, args.arquivo)
        elif args.funcao == 'estilo_rainbow' or args.funcao == '2':
            es.estilo_rainbow(args.filename, args.arquivo)
        else:
            print("Erro: Função não reconhecida no módulo estilo.")
            sys.exit(1)

    else:
        print("Erro: Módulo ou função não especificados corretamente.")
        sys.exit(1)


if __name__ == '__main__':
    Main()