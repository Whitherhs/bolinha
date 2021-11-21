import blocos
import nomedojogador

# Todos esses eventos são acionados de acordo com seus respectivos nomes

def jogo_abriu(janela):
    # Pode ser utilizado para posicionar elementos na tela, etc.
    print('JOGO ABRIU')
    blocos.desenhar_blocos(janela)
    nomedojogador.nomedojogadores(janela)


def loop_principal():
    pass


def colisao_bola_jogador():
    print('COLISÃO')


def fim_de_jogo():
    print('FIM DE JOGO')
