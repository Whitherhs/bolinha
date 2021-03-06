from graphics import *

import som

nome = ''

def tela_nome(janela, centro_tela, cor_principal, cor_secundaria):
    mensagem = Text(
        Point(centro_tela.getX(), centro_tela.getY() - 50),
        'Insira seu nome (3 letras): '
    )
    mensagem.setSize(18)
    mensagem.setTextColor(cor_principal)
    mensagem.draw(janela)

    nomejogador = Entry(Point(centro_tela.getX(), centro_tela.getY()), 20)
    nomejogador.setTextColor(cor_secundaria)
    nomejogador.setFill(cor_principal)
    nomejogador.draw(janela)

    while True:
        teclas = janela.checkKey()

        if teclas:
            som.som_menu()

        nome = nomejogador.getText().upper()
        if len(nomejogador.getText()) >= 3:
            mensagem.undraw()
            nomejogador.undraw()
            return nome
        update(60)