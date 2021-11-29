from graphics import *


def gravar_entrada(nome, pontos):
    f = open('ranking.txt', 'a')
    f.write(f'{nome}, {pontos}\n')
    f.close()


def ler_entradas():
    f = open('ranking.txt', 'r')
    ranking = f.readlines()
    f.close()

    return ranking

def desenhar_tela(janela, cor_principal, centro_tela):
    lista_objetos = []

    ranking = ler_entradas()

    t1 = Text(Point(centro_tela.getX(), 50), 'Melhores jogadores:')
    t1.setTextColor(cor_principal)
    t1.setSize(24)
    t1.draw(janela)
    lista_objetos.append(t1)

    texto_ranking = Text(Point(centro_tela.getX(), 150), ''.join(ranking))
    texto_ranking.setTextColor(cor_principal)
    texto_ranking.setSize(12)
    texto_ranking.draw(janela)
    lista_objetos.append(texto_ranking)
    
    janela.getMouse()

    for objeto in lista_objetos:
        objeto.undraw()
