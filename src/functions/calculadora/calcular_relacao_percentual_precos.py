from util.util import fim_funcao


def calcular_relacao_percentual_precos():
    precox = float(input("Digite o primeiro valor : "))
    precoy = float(input("Digite o segundo valor : "))
    percentual = precox / precoy * 100
    print("Percentual é de ", "{:,.2f}".format(percentual))
    fim_funcao()
