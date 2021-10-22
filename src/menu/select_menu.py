from getch import getch

from util.util import clean


def __selectMenu(valores, podeVoltar):
    clean()

    print(" Selecione a opção desejada")

    for key, value in valores.items():
        textoMenu = "       " + str(key) + " - " + value
        print(textoMenu)

    valoresAceitos = list(valores.keys())
    valoresAceitos.append(0)

    if (podeVoltar):
        print("       " + str(9) + " - Voltar")
        valoresAceitos.append(9)

    print("       " + str(0) + " - Finalizar o Programa")

    while True:
        try:
            opcao = int(getch())
            if (opcao in (valoresAceitos)):
                clean()
                break
        except:
            continue

    if opcao == 0:
        print("Finalizando...")
        exit(0)

    return opcao


def select_menu_principal(valores):
    return __selectMenu(valores, False)


def select_menu(valores):
    return __selectMenu(valores, True)
