from util.util import clean
from getch import getch
from math import ceil

def paginacao(items, cabecalho):
    qtdItemPorPagina = 20
    qtdItems = len(items)
    paginaAtual = 0
    totalPagina = ceil(qtdItems / qtdItemPorPagina)

    while True:
        primeiroItem = paginaAtual*qtdItemPorPagina
        ultimoItemPagina = int(primeiroItem +qtdItemPorPagina)

        if(ultimoItemPagina > qtdItems):
            ultimoItemPagina = qtdItems

        print(cabecalho + "\n")

        for index in range(primeiroItem, ultimoItemPagina):
            print(items[index])

        print()
        print("Pagina " + str(paginaAtual+1) + " de " + str(totalPagina))

        comando = __controlePagina(primeiroItem == 0, ultimoItemPagina == qtdItems)

        if(comando == 0):
            clean()
            break
        else:
            clean()
            paginaAtual += comando

def __controlePagina(isPrimeiraPagina, isUltimaPagina):
    print()
    print("N = Next, P = Previous, Q = Quit ")
    print()

    while True:
        comando = getch()

        match comando.lower():
            case "n":
                if(isUltimaPagina):
                    continue
                else:
                    return 1
            case "p":
                if(isPrimeiraPagina):
                    continue
                else:
                    return -1
            case "":
                if(isUltimaPagina):
                    continue
                else:
                    return 1
            case "q":
                return 0


