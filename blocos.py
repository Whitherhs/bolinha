from graphics import *

def desenhar_blocos(janela):
    comprimento = 50
    largura = 20
    borda = 25
    largura_tela = janela.getWidth()
    altura_tela = janela.getHeight()
    passo_horizontal = borda + comprimento
    passo_vertical = borda + largura
    quant_colunas = largura_tela // passo_horizontal
    quant_linhas = (altura_tela // 3) // passo_vertical

    blocos = []

    for i in range(1, quant_colunas):
        for j in range(1, quant_linhas + 1):
            bloco = Rectangle(
                Point(
                    i * passo_horizontal,
                    j * passo_vertical
                ),
                Point(
                    i * passo_horizontal + comprimento,
                    j * passo_vertical + largura
                )
            )
            bloco.setFill('white')
            bloco.draw(janela)
            blocos.append(bloco)
    
    return blocos
