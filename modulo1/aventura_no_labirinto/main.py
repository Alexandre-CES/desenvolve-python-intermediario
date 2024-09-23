''' Jogo: Aventura no labirinto

    Foi feito para ser jogado interagindo com o terminal. Para isso, foi utilizado a biblioteca pynput para obter inputs do terminal e a biblioteca rich para deixa-lo mais bonito
'''

import aventura_pkg

lab = aventura_pkg.labirinto
jog = aventura_pkg.jogador
uti = aventura_pkg.utils

def Main():

    #instanciando classes e funções
    args = uti.args()
    labirinto = lab.Labirinto()
    jogador = jog.Jogador()

    #Iniciando labirinto e jogador
    labirinto.criar_labirinto(args.dificuldade)
    jogador.iniciar_jogador()

    labirinto.imprimir_labirinto()

    uti.imprimir_instrucoes()


if __name__ == '__main__':
    Main()