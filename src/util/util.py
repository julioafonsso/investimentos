import os
from getch import getch

def fimFuncao():
    print("")

    print("Digite qualquer valor para voltar ...")
    getch()
    clean()


def clean():
    os.system('cls' if os.name=='nt' else 'clear')
