from graphics import *
import random

import eventos
import blocos


def jogo_base(janela, centro_tela, cor_principal, nome):
    # Variáveis de configuração da bolinha
    # X = horizontal, Y = vertical
    raio_bolinha = 15
    
    pos_inicial_bolinha = Point(
        centro_tela.getX(),
        centro_tela.getY() / 3 * 4
    )

    velocidade_inicial_bolinha_x = 3
    velocidade_inicial_bolinha_y = 4

    velocidade_bolinha_x = velocidade_inicial_bolinha_x
    velocidade_bolinha_y = velocidade_inicial_bolinha_y
    
    sentido_inicial_bolinha_x = 0
    sentido_inicial_bolinha_y = 1

    sentido_bolinha_x = sentido_inicial_bolinha_x
    sentido_bolinha_y = sentido_inicial_bolinha_y

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
    pontos = 0
    vidas = 3
    altura_barra_superior = 30

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

    # Barra superior
    barra_superior = Line(
        Point(0, altura_barra_superior),
        Point(janela.getWidth(), altura_barra_superior)
    )
    barra_superior.setFill(cor_principal)
    barra_superior.draw(janela)

    # Texto na tela
    texto_principal = Text(centro_tela,
        'Pressione qualquer tecla para iniciar.'
    )
    texto_principal.setTextColor(cor_principal)
    texto_principal.setSize(24)
    texto_principal.draw(janela)

    texto_nome = Text(
        Point(30, 15),
        nome.upper()
    )
    texto_nome.setTextColor(cor_principal)
    texto_nome.setSize(12)
    texto_nome.draw(janela)

    texto_pontos = Text(
        Point(centro_tela.getX(), 15),
        f'Pontos: {pontos}'
    )
    texto_pontos.setTextColor(cor_principal)
    texto_pontos.setSize(12)
    texto_pontos.draw(janela)

    # Blocos
    blocos_lista = blocos.desenhar_blocos(janela, cor_principal)

    # Corações
    coracoes = []
    pos_inicial_coracoes = janela.getWidth() - (16 * vidas + 15)
    for i in range(vidas):
        coracao = Image(Point(pos_inicial_coracoes + i * 20, 15), './img/coração.png')
        coracao.draw(janela)
        coracoes.append(coracao)

    # Jogo foi aberto
    eventos.jogo_abriu(janela)

    # Loop principal
    janela.getKey()

    contagem(texto_principal)
    texto_principal.undraw()

    while True:
        # Variáveis do loop
        pos_atual_bolinha = bolinha.getCenter()

        pos_atual_jogador = jogador.getCenter()

        lado_esquerdo_jogador = pos_atual_jogador.getX() - (comprimento_jogador / 2)
        lado_direito_jogador = pos_atual_jogador.getX() + (comprimento_jogador / 2)

        colisao_com_jogador_x = lado_esquerdo_jogador <= pos_atual_bolinha.getX() <= lado_direito_jogador
        colisao_com_jogador_y = pos_atual_bolinha.getY() >= pos_atual_jogador.getY()

        # Movimento da bolinha
        if pos_atual_bolinha.getX() <= 0 or pos_atual_bolinha.getX() >= janela.getWidth():
            # Bolinha bateu no lado direito ou esquerdo da tela
            sentido_bolinha_x *= -1

        if pos_atual_bolinha.getY() <= altura_barra_superior or pos_atual_bolinha.getY() >= pos_atual_jogador.getY():
            # Bolinha bateu no lado inferior ou superior da tela
            if colisao_com_jogador_x and colisao_com_jogador_y:
                # Colisão entre bolinha e jogador
                velocidade_bolinha_y = 4 + (random.randrange(1, pontos + 2) / 10)
                velocidade_bolinha_x = 3 + (random.randrange(1, pontos + 2) / 10)
                if sentido_bolinha_x == 0:
                    sentido_bolinha_x = random.choice((-1, 1))
                eventos.colisao_bola_jogador()

            elif colisao_com_jogador_y and not colisao_com_jogador_x:
                # Fim de jogo
                vidas -= 1

                coracoes[-1].undraw()
                coracoes.pop()

                if vidas > 0:
                    bolinha.undraw()
                    bolinha = Circle(pos_inicial_bolinha, raio_bolinha)
                    bolinha.setFill(cor_principal)
                    bolinha.draw(janela)

                    jogador.undraw()
                    jogador = Line(pos_inicial_jogador, Point(
                        pos_inicial_jogador.getX() + comprimento_jogador,
                        pos_inicial_jogador.getY())
                    )
                    jogador.setFill(cor_principal)
                    jogador.setWidth(largura_jogador)
                    jogador.draw(janela)

                    velocidade_bolinha_x = velocidade_inicial_bolinha_x
                    velocidade_bolinha_y = velocidade_inicial_bolinha_y

                    sentido_bolinha_x = sentido_inicial_bolinha_x
                    sentido_bolinha_y = sentido_inicial_bolinha_y

                    texto_principal.draw(janela)
                    texto_principal.setText('Tente novamente!')
                    time.sleep(1)
                    contagem(texto_principal)
                    texto_principal.undraw()

                else:
                    texto_principal.setText(f'FIM DE JOGO\n\nVocê marcou {pontos} pontos.')
                    texto_principal.draw(janela)
                    eventos.fim_de_jogo(nome, pontos)
                    break    

            sentido_bolinha_y *= -1

        bolinha.move(
            velocidade_bolinha_x * sentido_bolinha_x,
            velocidade_bolinha_y * sentido_bolinha_y
        )

        # Colisão com blocos
        for i in range(len(blocos_lista)):
            if blocos_lista[i] != '':
                lado_esquerdo_bloco = blocos_lista[i].getCenter().getX() - (50 / 2)
                lado_direito_bloco = blocos_lista[i].getCenter().getX() + (50 / 2)

                lado_superior_bloco = blocos_lista[i].getCenter().getY() - (20 / 2)
                lado_inferior_bloco = blocos_lista[i].getCenter().getY() + (20 / 2)

                colisao_com_bloco_x = lado_esquerdo_bloco <= pos_atual_bolinha.getX() <= lado_direito_bloco
                colisao_com_bloco_y = lado_superior_bloco <= pos_atual_bolinha.getY() <= lado_inferior_bloco

                if colisao_com_bloco_x and colisao_com_bloco_y:
                    blocos_lista[i].undraw()
                    blocos_lista[i] = ''
                    if blocos_lista[i] == '':
                        # Colisão com bloco
                        pontos += 1
                        sentido_bolinha_y *= -1
                        eventos.colisao_bola_bloco(janela, blocos_lista[i])

        # Movimento do jogador
        tecla = janela.checkKey()

        if tecla == 'Left':
            # Esquerda
            if lado_esquerdo_jogador > 0:
                jogador.move(- velocidade_jogador, 0)

        elif tecla == 'Right':
            # Direita
            if lado_direito_jogador < janela.getWidth():
                jogador.move(velocidade_jogador, 0)

        # Loop principal
        texto_pontos.setText(f'Pontos: {pontos}')
        eventos.loop_principal()

        # Jogador venceu
        if blocos_lista.count('') == len(blocos_lista) and blocos_lista:
            texto_principal.setText(f'Parabéns {nome}, você venceu! :)\nPontos: {pontos}')
            texto_principal.draw(janela)
            eventos.jogador_venceu(nome, pontos)
            break



        update(velocidade_jogo)

    janela.getMouse()
    janela.close()

def contagem(texto):
    for i in range(3, 0, -1):
        texto.setText(i)
        time.sleep(1)
    texto.setText('BOM JOGO!')
    time.sleep(1)