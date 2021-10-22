from functions.calculadora.aplicar_percentual import aplicarPercentualPreco
from functions.calculadora.calcular_diferenca_percentual_preco import calcularDiferenPercentualPrecos
from functions.calculadora.calcular_relacao_percentual_precos import calcular_relacao_percentual_precos
from functions.calculadora.projecao_investimento import projecao_investimento
from menu.select_menu import selectMenu


def calculadora():
    while True:
        opcaoMenu = selectMenu({
            1: "Diferença percentual entre preços",
            2: "Aplicar um percentual ao preço",
            3: "Calcular Relação Percentual de Preços",
            4: "Projeção Investimento",
            9: "Voltar Menu Principal",
            0: "Encerrar"
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
            case 0:
                exit(0)
