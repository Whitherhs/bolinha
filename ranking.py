from graphics import *


def ranking(janela):
    leitura = open('placar.txt', 'r')
    for nomes in leitura:
        message = Text(Point(400, 300), nomes)
        message.setFill("white")
        message.draw(janela)
    leitura.close()


    print('Fim de leitura do arquivo')

