from simple_term_menu import TerminalMenu

from util.util import clean


class Menu:

    def __init__(self, valores, permite_voltar_menu = True):
        self.labels = []
        self.functions = []
        self.permite_voltar_menu = permite_voltar_menu

        for key, value in valores.items():
            self.labels.append(key)
            self.functions.append(value)
        if permite_voltar_menu:
            self.labels.append("Voltar")
        else:
            self.labels.append("Sair")

    def show_menu(self):

        while True:

            clean()
            print(" Selecione a opção desejada")

            menu_entry_index = TerminalMenu(self.labels).show()

            if(len(self.labels)- 1 == menu_entry_index):
                break

            self.functions[menu_entry_index]()

