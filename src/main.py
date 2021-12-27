from functions.acoes.listar_acoes_b3 import listar_acoes
from functions.acoes.listar_opcoes_b3 import listar_opcoes
from functions.calculadora.aplicar_percentual import aplicar_percentual_preco
from functions.calculadora.calcular_diferenca_percentual_preco import calcular_diferenca_percentual_precos
from functions.calculadora.calcular_relacao_percentual_precos import calcular_relacao_percentual_precos
from functions.calculadora.projecao_investimento import projecao_investimento
from menu.menu import Menu

menu_calculadora = {
    "Diferença percentual entre preços": calcular_diferenca_percentual_precos,
    "Aplicar um percentual ao preço": aplicar_percentual_preco,
    "Calcular Relação Percentual de Preços": calcular_relacao_percentual_precos,
    "Projeção Investimento": projecao_investimento
}

menu_acoes = {
    'Listar Acoes Ibovespa': listar_acoes,
    'Listar Opções Ibovespa': listar_opcoes
}

menu_principal = {
    'Calculadora': Menu(menu_calculadora).show_menu,
    'Acoes': Menu(menu_acoes).show_menu
}

menu = Menu(menu_principal, False).show_menu()
