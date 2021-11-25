from graphics import *

import menu
import base
import jogador

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
    escolha = menu.menu(janela, centro_tela)
    if escolha == 1:
        nome = jogador.tela_nome(janela, centro_tela, cor_principal, cor_secundaria)
        base.jogo_base(janela, centro_tela, cor_principal, nome)

    else:
        texto = Text(Point(centro_tela.getX(), centro_tela.getY()), 'Não implementado')
        texto.setSize(24)
        texto.setTextColor(cor_principal)
        texto.draw(janela)
        janela.getMouse()
        janela.close()

if __name__ == '__main__':
    main()