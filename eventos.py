import ranking

# Todos esses eventos são acionados de acordo com seus respectivos nomes

def jogo_abriu(janela):
    # Pode ser utilizado para posicionar elementos na tela, etc.
    print('JOGO ABRIU')


def loop_principal():
    pass


def colisao_bola_jogador():
    print('COLISÃO JOGADOR')


def colisao_bola_bloco(janela, bloco):
    print('COLISÃO BLOCO')


def fim_de_jogo(nome, pontos):
    print('FIM DE JOGO')
    ranking.gravar_entrada(nome, pontos)

def jogador_venceu(nome, pontos):
    print('JOGADOR VENCEU')
    ranking.gravar_entrada(nome, pontos)