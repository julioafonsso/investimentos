from datetime import datetime

from model.lista import Lista
from util.getchar import GetChar
from util.util import clean
from math import ceil


def paginacao(lista: Lista):
    qtdItemPorPagina = 20
    paginaAtual = 0
    qtdItems = len(lista.get_lista())
    totalPagina = ceil(qtdItems / qtdItemPorPagina)
    while True:
        clean()
        primeiroItem = paginaAtual * qtdItemPorPagina

        ultimoItemPagina = int(primeiroItem + qtdItemPorPagina)

        if ultimoItemPagina > qtdItems:
            ultimoItemPagina = qtdItems

        print(lista.cabecalho() + "\n")

        for index in range(primeiroItem, ultimoItemPagina):
            print(lista.get_lista()[index].print())

        print()
        print("Pagina " + str(paginaAtual + 1) + " de " + str(totalPagina))
        print()
        print("S = Sair, F = Filtar, O = Ordenar, L = Limpar, P = Print ")

        isUltimaPagina = ultimoItemPagina == qtdItems
        isPrimeiraPagina = primeiroItem == 0
        while True:
            comando = GetChar().get_value()

            match comando:
                case GetChar.RIGHT_KEY:
                    if isUltimaPagina:
                        continue
                    else:
                        paginaAtual += 1
                        break
                case GetChar.LEFT_KEY:
                    if isPrimeiraPagina:
                        continue
                    else:
                        paginaAtual -= 1
                        break
                case "s":
                    return
                case "o":
                    clean()
                    lista.ordernar()
                    paginaAtual = 0
                    break
                case "l":
                    clean()
                    lista.limpar_filtro()
                    paginaAtual = 0
                    qtdItems = len(lista.get_lista())
                    totalPagina = ceil(qtdItems / qtdItemPorPagina)
                    break
                case "f":
                    clean()
                    lista.filtrar()
                    paginaAtual = 0
                    qtdItems = len(lista.get_lista())
                    totalPagina = ceil(qtdItems / qtdItemPorPagina)
                    break
                case "p":
                    clean()
                    print("digite o nome do arquivo.")
                    nome = input()
                    nome_arquivo = "/home/julio/investimentos/" + str(nome) + "_" + datetime.now().strftime(
                        "%Y%m%d_%H%M%S") + ".txt"

                    arquivo = open(nome_arquivo, 'w')
                    arquivo.write(lista.cabecalho())
                    arquivo.write("\n")
                    for item in lista.get_lista():
                        arquivo.write(item.print())
                        arquivo.write("\n")
                    arquivo.close()
                    break
