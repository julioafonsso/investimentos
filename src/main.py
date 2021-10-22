from menu.calculadora import calculadora
from menu.listAcoes import  listarAcoes
from menu.select_menu import selectMenu

while True:

    opcaoMenu = selectMenu({1: "Calculadora",
                            2: "Listar ações",
                            0: "Saida"})
    match opcaoMenu:
        case 1:
            calculadora()
        case 2:
            listarAcoes()
        case 0:
            break

print("Finalizando...")
