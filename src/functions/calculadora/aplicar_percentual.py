from util.util import fimFuncao


def aplicarPercentualPreco():
    preco = float(input("Digite o Preço : "))
    percentual = float(input("Digite o Percentual : "))

    valorFinal = preco * percentual / 100
    print("O valor final é ", valorFinal)
    fimFuncao()