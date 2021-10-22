from functions.listar_ativos.listar_ativos_nasdaq import listar_ativos_nasdaq
from functions.listar_ativos.listar_ativos_sp500 import listar_ativos_sp500
from functions.listar_ativos.listar_ativos_ibovespa import listarAtivosIbovespa
from menu.select_menu import selectMenu


def listarAcoes():
    opcaoMenu = selectMenu({
        1: 'Ativos do Indice Ibovespa',
        2: 'Ativos do SP500',
        3: 'Ativos da NASDAQ'
    })

    match opcaoMenu:
        case 1:
            listarAtivosIbovespa()
        case 2:
            listar_ativos_sp500()
        case 3:
            listar_ativos_nasdaq()
