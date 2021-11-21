from graphics import *
import random

import eventos

# Tela do jogo
janela = GraphWin('Bolinha', 800, 600)
janela.setBackground('#000')

# Centro da tela
centro_tela = Point(
    janela.getWidth() / 2,
    janela.getHeight() / 2
)

# Variáveis de configuração da bolinha
# X = horizontal, Y = vertical
raio_bolinha = 15

pos_inicial_bolinha = Point(
    centro_tela.getX(),
    centro_tela.getY() / 2
)

velocidade_bolinha_x = 3
velocidade_bolinha_y = 4

sentido_bolinha_x = random.choice((-1, 1))
sentido_bolinha_y = 1

# Variáveis de configuração do jogador (barra)
comprimento_jogador = 150
largura_jogador = 20

pos_inicial_jogador = Point(
    (janela.getWidth() - comprimento_jogador) / 2,
    janela.getHeight() - largura_jogador
)

velocidade_jogador = 30

# Variáveis de configuração do jogo
velocidade_jogo = 60
cor_principal = '#fff'
pontos = 0

# Bolinha
bolinha = Circle(pos_inicial_bolinha, raio_bolinha)
bolinha.setFill(cor_principal)
bolinha.draw(janela)

# Jogador
jogador = Line(pos_inicial_jogador, Point(
    pos_inicial_jogador.getX() + comprimento_jogador,
    pos_inicial_jogador.getY())
)
jogador.setFill(cor_principal)
jogador.setWidth(largura_jogador)
jogador.draw(janela)

# Texto na tela
texto = Text(centro_tela,
    'Pressione qualquer tecla para iniciar.'
)
texto.setTextColor(cor_principal)
texto.setSize(24)
texto.draw(janela)

# Jogo foi aberto
eventos.jogo_abriu(janela)

# Loop principal
janela.getKey()

while True:
    # Variáveis do loop
    pos_atual_bolinha = bolinha.getCenter()

    pos_atual_jogador = jogador.getCenter()

    lado_esquerdo_jogador = pos_atual_jogador.getX() - (comprimento_jogador / 2)
    lado_direito_jogador = pos_atual_jogador.getX() + (comprimento_jogador / 2)

    colisao_com_jogador_x = lado_esquerdo_jogador <= pos_atual_bolinha.getX() <= lado_direito_jogador
    colisao_com_jogador_y = pos_atual_bolinha.getY() >= pos_atual_jogador.getY()

    # Loop principal
    texto.setText(f'Pontos: {pontos}')
    eventos.loop_principal()

    # Movimento da bolinha
    if pos_atual_bolinha.getX() <= 0 or pos_atual_bolinha.getX() >= janela.getWidth():
        # Bolinha bateu no lado direito ou esquerdo da tela
        sentido_bolinha_x *= -1

    if pos_atual_bolinha.getY() <= 0 or pos_atual_bolinha.getY() >= pos_atual_jogador.getY():
        # Bolinha bateu no lado inferior ou superior da tela
        if colisao_com_jogador_x and colisao_com_jogador_y:
            # Colisão entre bolinha e jogador
            pontos += 1
            velocidade_bolinha_y += (random.randrange(1, pontos + 2) / 10)
            velocidade_bolinha_x += (random.randrange(1, pontos + 2) / 10)
            eventos.colisao_bola_jogador()

        elif colisao_com_jogador_y and not colisao_com_jogador_x:
            # Fim de jogo
            texto.setText(f'FIM DE JOGO\n\nVocê marcou {pontos} pontos.')
            eventos.fim_de_jogo()
            break

        sentido_bolinha_y *= -1

    bolinha.move(
        velocidade_bolinha_x * sentido_bolinha_x,
        velocidade_bolinha_y * sentido_bolinha_y
    )

    # Movimento do jogador
    tecla = janela.checkKey()

    if tecla == 'Left':
        # Esquerda
        jogador.move(- velocidade_jogador, 0)

    elif tecla == 'Right':
        # Direita
        jogador.move(velocidade_jogador, 0)

    update(velocidade_jogo)

janela.getMouse()
janela.close()
