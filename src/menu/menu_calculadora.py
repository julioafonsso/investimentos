from functions.calculadora.aplicar_percentual import aplicarPercentualPreco
from functions.calculadora.calcular_diferenca_percentual_preco import calcularDiferenPercentualPrecos
from functions.calculadora.calcular_relacao_percentual_precos import calcular_relacao_percentual_precos
from functions.calculadora.projecao_investimento import projecao_investimento
from menu.select_menu import select_menu


def menu_calculadora():
    while True:
        opcaoMenu = select_menu({
            1: "Diferença percentual entre preços",
            2: "Aplicar um percentual ao preço",
            3: "Calcular Relação Percentual de Preços",
            4: "Projeção Investimento"
        })

        match opcaoMenu:
            case 1:
                calcularDiferenPercentualPrecos()
            case 2:
                aplicarPercentualPreco()
            case 3:
                calcular_relacao_percentual_precos()
            case 4:
                projecao_investimento()
            case 9:
                break
