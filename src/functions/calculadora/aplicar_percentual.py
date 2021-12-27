from util.util import fim_funcao


def aplicar_percentual_preco():
    preco = float(input("Digite o Preço : "))
    percentual = float(input("Digite o Percentual : "))

    valorFinal = preco * percentual / 100
    print("O valor final é ", valorFinal)
    fim_funcao()
