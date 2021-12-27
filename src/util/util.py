import os
from getch import getch


def fim_funcao():
    print("")

    print("Digite qualquer valor para voltar ...")
    getch()
    clean()


def clean():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###########################################################################")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                        CONTROLE DE INVESTIMENTOS                        #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("###########################################################################")
    print()
    print()


def captura_inteiro(label) -> int:
    while True:
        try:
            print(label)
            print()
            valor = int(input())
            return valor
        except:
            print("Valor invalido.")


def converte_string_para_float(valor):
    return float(valor.replace("%", "").replace(".", "").replace(",", "."))
