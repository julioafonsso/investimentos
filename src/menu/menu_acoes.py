from functions.infos.get_info import get_info
from menu.select_menu import select_menu


def menu_acoes():
    while True:
        opcaoMenu = select_menu({
            1: 'Obter Informações de uma Ação'
        })

        match opcaoMenu:
            case 1:
                get_info()
            case 9:
                break
