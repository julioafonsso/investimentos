from getch import getch

from util.util import clean


def selectMenu(valores):
    clean()


    print(" Selecione a opção desejada")

    for key, value in valores.items():
        textoMenu = "       " + str(key) + " - " + value
        print(textoMenu)

    while True:
        try:
            opcao = int(getch())
            clean()
            break
        except:
            continue

    return opcao
