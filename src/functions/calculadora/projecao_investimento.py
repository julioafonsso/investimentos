from util.util import fim_funcao


def projecao_investimento():
    qtdAnos = int(input("Digite o numero de anos : "))
    valorInicial = float(input("Digite o valor inicial : "))
    aporteMensal = float(input("Digite o valor de aporte mensal : "))
    taxaMediaAnual = float(input("Digite a taxa media de juros anual : "))

    valorTotal = valorInicial
    for i in range(0, qtdAnos):
        valorTotal += aporteMensal * 12
        valorTotal += valorTotal * (taxaMediaAnual / 100)
        print("ano " + str(i + 1).ljust(2) + " Valor Total : " + "${:,.2f}".format(valorTotal))

    rendimentoAnualFinal = valorTotal * taxaMediaAnual / 100

    print("O valor medio calculado é de ", "${:,.2f}".format(valorTotal))

    print("Rendimento anual no fim de " + str(qtdAnos) + " ano(s) será de "  "${:,.2f}".format(rendimentoAnualFinal))

    print("Rendimento mensal no fim de " + str(qtdAnos) + " ano(s) será de "  "${:,.2f}".format(
        rendimentoAnualFinal / 12))
    fim_funcao()
