from graphics import *

import menu
import base
import jogador
import ranking

# Cores
cor_principal = '#fff'
cor_secundaria = '#000'

# Tela do jogo
janela = GraphWin('Bolinha', 800, 600)
janela.setBackground(cor_secundaria)

# Centro da tela
centro_tela = Point(
    janela.getWidth() / 2,
    janela.getHeight() / 2
)

def main():
    while True:
        escolha = menu.menu(janela, centro_tela)
        if escolha == 1:
            nome = jogador.tela_nome(janela, centro_tela, cor_principal, cor_secundaria)
            base.jogo_base(janela, centro_tela, cor_principal, nome)
        elif escolha == 4:
            ranking.desenhar_tela(janela, cor_principal, centro_tela)
        else:
            texto = Text(Point(centro_tela.getX(), centro_tela.getY()), 'Não implementado')
            texto.setSize(24)
            texto.setTextColor(cor_principal)
            texto.draw(janela)
            janela.getMouse()
            janela.close()
            break

if __name__ == '__main__':
    main()
