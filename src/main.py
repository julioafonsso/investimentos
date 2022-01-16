from functions.calculadora.aplicar_percentual import aplicar_percentual_preco
from functions.calculadora.calcular_diferenca_percentual_preco import calcular_diferenca_percentual_precos
from functions.calculadora.calcular_relacao_percentual_precos import calcular_relacao_percentual_precos
from functions.calculadora.projecao_investimento import projecao_investimento
from functions.listas.listar_acoes_ibovespa import listar_acoes_ibovespa
from functions.listas.listar_opcoes_ibovespa import listar_opcoes_ibovespa
from functions.listas.listar_fundos_imobiliarios import listar_fundos_imobiliarios
from menu.menu import Menu

menu_calculadora = {
    "Diferença percentual entre preços": calcular_diferenca_percentual_precos,
    "Aplicar um percentual ao preço": aplicar_percentual_preco,
    "Calcular Relação Percentual de Preços": calcular_relacao_percentual_precos,
    "Projeção Investimento": projecao_investimento
}

menu_lista_ibovespa = {
    'Listar Acoes Ibovespa': listar_acoes_ibovespa,
    'Listar Fundos Imobiliarios': listar_fundos_imobiliarios,
    'Listar Opções Ibovespa': listar_opcoes_ibovespa

}

menu_principal = {
    'Calculadora': Menu(menu_calculadora).show_menu,
    'Lista Ibovespa': Menu(menu_lista_ibovespa).show_menu
}

menu = Menu(menu_principal, False).show_menu()
