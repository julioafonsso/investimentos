from menu.menu_calculadora import menu_calculadora
from menu.menu_indices import  menu_indices
from menu.select_menu import select_menu_principal

while True:

    opcaoMenu = select_menu_principal({1: "Calculadora",
                                       2: "Indices"})
    match opcaoMenu:
        case 1:
            menu_calculadora()
        case 2:
            menu_indices()
