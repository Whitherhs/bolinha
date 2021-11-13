from graphics import *
import random

# Tela do jogo
janela = GraphWin('Bolinha', 800, 600)
janela.setBackground('#000')

# Variáveis de configuração
raio_bolinha = 15

pos_inicial_bolinha_x = janela.getWidth() / 2
pos_inicial_bolinha_y = janela.getHeight() / 4

velocidade_bolinha_x = 3
velocidade_bolinha_y = 4

sentido_bolinha_x = random.choice((-1, 1))
sentido_bolinha_y = 1

comprimento_jogador = 150
largura_jogador = 20

pos_inicial_jogador_x = (janela.getWidth() - comprimento_jogador) / 2
pos_jogador_y = janela.getHeight() - largura_jogador

velocidade_jogador = 30

velocidade_jogo = 60

pontos = 0

cor_principal = '#fff'

# Bolinha
bolinha = Circle(
    Point(pos_inicial_bolinha_x, pos_inicial_bolinha_y),
    raio_bolinha
)
bolinha.setFill(cor_principal)
bolinha.draw(janela)

# Jogador
jogador = Line(
    Point(pos_inicial_jogador_x, pos_jogador_y),
    Point(pos_inicial_jogador_x + comprimento_jogador, pos_jogador_y)
)
jogador.setFill(cor_principal)
jogador.setWidth(largura_jogador)
jogador.draw(janela)

# Texto na tela
texto = Text(
    Point(janela.getWidth() / 2, janela.getHeight() / 2),
    'Pressione qualquer tecla para iniciar.'
)
texto.setTextColor(cor_principal)
texto.setSize(24)
texto.draw(janela)

# Loop principal
janela.getKey()

while True:
    texto.setText(f'Pontos: {pontos}')

    # Movimento da bolinha
    pos_bolinha_x = bolinha.getCenter().getX()
    pos_bolinha_y = bolinha.getCenter().getY()

    pos_jogador_x = jogador.getCenter().getX()

    colisao_com_jogador_x = pos_jogador_x + (comprimento_jogador / 2) >= pos_bolinha_x >= pos_jogador_x - (comprimento_jogador / 2)
    colisao_com_jogador_y = pos_bolinha_y >= pos_jogador_y

    if pos_bolinha_x <= 0 or pos_bolinha_x >= janela.getWidth():
        sentido_bolinha_x *= -1

    if pos_bolinha_y <= 0 or pos_bolinha_y >= pos_jogador_y:
        if colisao_com_jogador_x and colisao_com_jogador_y:
            # Colisão entre bolinha e jogador
            print('Colisão')
            pontos += 1
            velocidade_bolinha_y += (random.randrange(1, pontos + 2) / 10)
            velocidade_bolinha_x += (random.randrange(1, pontos + 2) / 10)
            print('Vel X:', velocidade_bolinha_x)
            print('Vel Y:', velocidade_bolinha_y)

        elif colisao_com_jogador_y and not colisao_com_jogador_x:
            # Fim de jogo
            texto.setText(f'FIM DE JOGO\n\nVocê marcou {pontos} pontos.')
            break

        sentido_bolinha_y *= -1

    bolinha.move(
        velocidade_bolinha_x * sentido_bolinha_x,
        velocidade_bolinha_y * sentido_bolinha_y
    )

    # Movimento do jogador
    tecla = janela.checkKey()

    if tecla == 'Left':
        jogador.move(- velocidade_jogador, 0)

    elif tecla == 'Right':
        jogador.move(velocidade_jogador, 0)

    update(velocidade_jogo)

janela.getMouse()
janela.close()
