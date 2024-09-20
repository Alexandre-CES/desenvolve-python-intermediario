'''
    Estilizar texto/arquivo com base nos argumentos passados por comando

    Foi feito utilizando a biblioteca -rich-, que permite personalizar as saídas no terminal. Esse programa é focado especificamente nas funções: estilo, layout, painel e progresso.

    Ao executar o programa, é necessário especificar o módulo e função desejados, por nome ou id, (podem ser conferidos passando a opção -h) para que o programa rode.

    exemplo de uso: 
        python3 main.py -a exemplo.txt -m 4 -f 2
'''

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
    [2]painel -> [1]painel_simples
    [3]progresso -> [1]barra_progresso, [2]barra_progresso_tasks
    [4]estilo -> [1]estilo_negrito, [2]estilo_rainbow'''
    )

    args = parser.parse_args()

    #colocar apenas função sem especificar o módulo resultará no encerramento do programa
    if args.funcao and not args.modulo:
        print("Erro: Você deve especificar um módulo com a opção -m antes de usar -f.")
        sys.exit(1)

    #como as funções layout e painel só possuem uma função acessível por comando, decidi que ativarão apenas chamando o módulo, sem precisar especificar a função
    if args.modulo == 'layout' or args.modulo == '1':
        la.print_layout(args.filename, args.arquivo)
    elif args.modulo == 'painel' or args.modulo == '2':
        pa.painel_simples(args.filename, args.arquivo)

    #O restante das funções precisam obrigatoriamente serem especificadas, ou resultará em erro
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
        print("Erro: Módulo não especificado corretamente.")
        sys.exit(1)


if __name__ == '__main__':
    Main()