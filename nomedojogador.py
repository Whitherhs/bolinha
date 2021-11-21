from graphics import *

def nomedojogadores(janela):
    mensagem2=Text(Point(400,250),"Nome do jogador")
    mensagem2.setSize(18)
    mensagem2.draw(janela)
    nomejogador = Entry(Point(400, 300), 3)
    nomejogador.draw(janela)

    nome=Text(Point(50, 30),"")
    nome.draw(janela)




    while True:
        nome.setText(nomejogador.getText())
        if len(nomejogador.getText()) > 3:
            break
        print("sucesso")