# Todos esses eventos são acionados de acordo com seus respectivos nomes

def jogo_abriu():
    # Pode ser utilizado para posicionar elementos na tela, etc.
    print('JOGO ABRIU')
    # criação de blocos
    posi1 = 100
    posi2 = 150
    posi3 = 100
    posi4 = 150
    posi5 = 100
    posi6 = 150
    posi7 = 100
    posi8 = 150
    blocos = Rectangle(Point(posi1, 30), Point(posi2, 10))
    blocos2 = Rectangle(Point(posi1, 100), Point(posi2, 80))
    blocos3 = Rectangle(Point(posi1, 170), Point(posi2, 150))
    blocos4 = Rectangle(Point(posi1, 240), Point(posi2, 220))
    blocos.setFill("white")
    blocos.draw(janela)
    blocos2.setFill("white")
    blocos2.draw(janela)
    blocos3.setFill("white")
    blocos3.draw(janela)
    blocos4.setFill("white")
    blocos4.draw(janela)
    # fileira1
    while True:
        posi1 += 80
        posi2 += 80
        blocos = Rectangle(Point(posi1, 30), Point(posi2, 10))
        blocos.setFill("white")
        blocos.draw(janela)

        if posi1 == 750 or posi2 > 750:
            break
    # fileira2
    while True:
        posi3 += 80
        posi4 += 80
        blocos2 = Rectangle(Point(posi3, 100), Point(posi4, 80))
        blocos2.setFill("white")
        blocos2.draw(janela)

        if posi3 == 750 or posi4 > 750:
            break
    # fileira3
    while True:
        posi5 += 80
        posi6 += 80
        blocos3 = Rectangle(Point(posi5, 170), Point(posi6, 150))
        blocos3.setFill("white")
        blocos3.draw(janela)
        if posi5 == 750 or posi6 > 750:
            break

    # fileira3
    while True:
        posi7 += 80
        posi8 += 80
        blocos4 = Rectangle(Point(posi7, 240), Point(posi8, 220))
        blocos4.setFill("white")
        blocos4.draw(janela)
        if posi7 == 750 or posi8 > 750:
            break


def loop_principal():
    pass


def colisao_bola_jogador():
    print('COLISÃO')


def fim_de_jogo():
    print('FIM DE JOGO')
