from util.util import fim_funcao


def calcular_diferenca_percentual_precos():
    precox = float(input("Digite o valor atual : "))
    precoy = float(input("Digite o valor esperado : "))
    percentual = precoy * 100 / precox
    print("A diferença percentual é de ", percentual - 100)
    fim_funcao()
