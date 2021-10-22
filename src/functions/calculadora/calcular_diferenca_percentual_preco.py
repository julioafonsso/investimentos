from util.util import fimFuncao


def calcularDiferenPercentualPrecos():
    precox = float(input("Digite o primeiro valor : "))
    precoy = float(input("Digite o segundo valor : "))
    percentual = precoy * 100 / precox
    print("A diferença percentual é de ", percentual - 100)
    fimFuncao()