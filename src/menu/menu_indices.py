from functions.listar_ativos_indices.listar_ativos_nasdaq import listar_ativos_nasdaq
from functions.listar_ativos_indices.listar_ativos_sp500 import listar_ativos_sp500
from functions.listar_ativos_indices.listar_ativos_ibovespa import listar_ativos_ibovespa
from menu.select_menu import select_menu


def menu_indices():
    opcaoMenu = select_menu({
        1: 'Listar Ativos do Indice Ibovespa',
        2: 'Listar Ativos do SP500',
        3: 'Listar Ativos da NASDAQ'
    })

    match opcaoMenu:
        case 1:
            listar_ativos_ibovespa()
        case 2:
            listar_ativos_sp500()
        case 3:
            listar_ativos_nasdaq()
