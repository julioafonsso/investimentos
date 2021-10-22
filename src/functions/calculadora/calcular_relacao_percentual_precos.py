from util.util import fimFuncao


def calcular_relacao_percentual_precos():
    precox = float(input("Digite o primeiro valor : "))
    precoy = float(input("Digite o segundo valor : "))
    percentual =  precox / precoy * 100
    print("Percentual é de ", percentual)
    fimFuncao();