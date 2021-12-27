from util.util import fim_funcao, clean


def projecao_investimento():
    qtdAnos = int(input("Digite o numero de anos : "))
    valorInicial = float(input("Digite o valor inicial : "))
    aporteMensal = float(input("Digite o valor de aporte mensal : "))
    taxaMediaAnual = float(input("Digite a taxa media de juros anual : "))

    valorTotal = valorInicial
    clean()
    print("ANO   | Valor Acumulado | Rendimento Anual | Rendimento Mensal")
    for i in range(0, qtdAnos):
        rendimento = valorTotal * (taxaMediaAnual / 100)
        aporteAnual = aporteMensal * 12
        valorTotal += rendimento + aporteAnual
        print(str(i).rjust(6) + "|" +
              "${:,.2f}".format(valorTotal).rjust(17) + "|" +
              "${:,.2f}".format(rendimento).rjust(18) + "|" +
              "${:,.2f}".format(rendimento/12).rjust(18))


    fim_funcao()
