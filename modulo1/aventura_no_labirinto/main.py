''' Jogo: Aventura no labirinto

    Foi feito para ser jogado interagindo com o terminal. Para isso, foi utilizado a biblioteca pynput para monitorar inputs do terminal e ajudar na movimentação do jogador e a biblioteca rich para deixa-lo mais bonito

'''
import sys
import aventura_pkg
from pynput import keyboard
import simpleaudio as sa
import threading

lab = aventura_pkg.labirinto
jog = aventura_pkg.jogador
uti = aventura_pkg.utils

class JogoAventuraLabirinto:
    '''Representa o jogo'''

    def __init__(self):
        self.jogador = jog.Jogador()
        self.labirinto = lab.Labirinto()
        self.jogo_ativo = True

    def Main(self):
        '''Onde o jogo é iniciado, começando pelo menu'''

        args = uti.args()

        if args.sound:
            threading.Thread(target=self.tocar_som).start()

        #Iniciando labirinto
        self.labirinto.criar_labirinto(args.dificuldade)

        #Começando jogo pelo menu
        uti.tela_inicial()

        #iniciar jogador
        self.jogador.iniciar_jogador(args.nome)

        #iniciando jogo
        self.andando_no_labirinto()

        #finalizando o jogo
        uti.finalizar_jogo(self.jogador,args.dificuldade)

    def andando_no_labirinto(self):
        '''Onde o jogo principal ocorre
        
        É uma função recursiva, que só finaliza quando o jogador está na saída do labirinto. A cada uma das iterações, o keyboard listener do pynput será chamado. Caso o jogador esteja na saída, todas as chamadas de andando_no_labirinto(self) serão encerradas.'''

        print()
        self.labirinto.imprimir_labirinto(self.jogador.posicao)

        #preparando listener do teclado
        with keyboard.Listener(on_release=self.on_release) as listener:
            listener.join()
        listener = keyboard.Listener(on_release=self.on_release)

        #a função se chamará até que o jogador ache a saída
        if self.jogador.posicao == self.labirinto.posicao_final:
            self.labirinto.imprimir_labirinto(self.jogador.posicao)
            return
        
        #recursividade
        if self.jogo_ativo:
            self.andando_no_labirinto()
        else:
            print('Tchau! ')
            sys.exit()

    def on_release(self,key):
        '''Andar no labirinto
        
        é utilizado um switch case para definir para onde o jogador moverá, com base no input. A lógica em si é simples, pegamos o x e y atual do jogador, acrescentando ou diminuindo em 1 de acordo com a direção. Mas não fará nada se a o local que o jogador deseja ir é uma parede ou fora dos limites'''

        x,y = self.jogador.posicao
        
        try:
            match key:
                case keyboard.Key.esc: #Sair do jogo
                    self.jogo_ativo = False
                case keyboard.Key.up:
                    y = max(y - 1, 0)
                    if self.labirinto.labirinto[y][x] != '#':
                        self.jogador.mover((x,y))
                case keyboard.Key.down:
                    y += 1
                    if self.labirinto.labirinto[y][x] != '#':
                        self.jogador.mover((x,y))
                case keyboard.Key.left:
                    x -= 1
                    if self.labirinto.labirinto[y][x] != '#':
                        self.jogador.mover((x,y))
                case keyboard.Key.right:
                    x += 1
                    if self.labirinto.labirinto[y][x] != '#':
                        self.jogador.mover((x,y))
        except IndexError:
            print('índice passando do limite')
        
        return False #Parar de monitorar 

    def tocar_som(self):
        '''Toca a música colocada nos assets'''

        wave_obj = sa.WaveObject.from_wave_file('./assets/sound.wav')
        play_obj = wave_obj.play()
        return play_obj

if __name__ == '__main__':
    jogo = JogoAventuraLabirinto()
    jogo.Main()