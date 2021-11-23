from graphics import *
from graphics import GraphWin

win = GraphWin('ball word', 800, 600)

escolha = 1
escmax = 4

nome = Text(Point(400, 100), "Ball Word")
nome.setFill("red")
nome.setSize(36)
nome.draw(win)

x = 100
y = 200

blocos = Rectangle(Point(x, y), Point(x + 200, y + 100))
blocos.setFill("black")
blocos.draw(win)

vspc = Rectangle(Point(x, y + 200), Point(x + 200, y + 300))
vspc.setFill("black")
vspc.draw(win)

x = 500

vsps = Rectangle(Point(x, y), Point(x + 200, y + 100))
vsps.setFill("black")
vsps.draw(win)

rank = Rectangle(Point(x, y + 200), Point(x + 200, y + 300))
rank.setFill("black")
rank.draw(win)

text = Text(blocos.getCenter(), "Blocos")
text.setSize(15)
text.setFill("green")
text.draw(win)

text = Text(vspc.getCenter(), "VS BOT")
text.setSize(15)
text.setFill("green")
text.draw(win)

text = Text(vsps.getCenter(), "1 VS 1")
text.setSize(15)
text.setFill("green")
text.draw(win)

op2text = Text(rank.getCenter(), "Placar")
op2text.setSize(15)
op2text.setFill("green")
op2text.draw(win)

blocosSele = Rectangle(blocos.getP1(), blocos.getP2())
blocosSele.setWidth(8)
blocosSele.setOutline("red")

vspcSele = Rectangle(vspc.getP1(), vspc.getP2())
vspcSele.setWidth(8)
vspcSele.setOutline("red")

vspsSele = Rectangle(vsps.getP1(), vsps.getP2())
vspsSele.setWidth(8)
vspsSele.setOutline("red")

rankSele = Rectangle(rank.getP1(), rank.getP2())
rankSele.setWidth(8)
rankSele.setOutline("red")

while True:
    teclas = win.checkKey()

    if teclas == "Down":
        if escolha == escmax:
            escolha = 1
        else:
            escolha += 1
    if teclas == "Up":
        if escolha == 1:
            escolha = escmax
        else:
            escolha -= 1

    if escolha == 1:
        rankSele.undraw()
        vspcSele.undraw()
        blocosSele.undraw()
        blocosSele.draw(win)

    if escolha == 2:
        vspsSele.undraw()
        blocosSele.undraw()
        vspcSele.undraw()
        vspcSele.draw(win)

    if escolha == 3:
        rankSele.undraw()
        vspcSele.undraw()
        vspsSele.undraw()
        vspsSele.draw(win)

    if escolha == 4:
        vspsSele.undraw()
        blocosSele.undraw()
        rankSele.undraw()
        rankSele.draw(win)

    if teclas == "Return":
        if escolha == 1:
            print("1")
            break
        if escolha == 2:
            print("2")
            break
        if escolha == 3:
            print("3")
            break
        if escolha == 4:
            print("4")
            break

    if teclas == "Escape":
        break
    update(30)

win.close()
