from model.opcao.lista_opcao import ListaOpcoes
from util.paginacao import paginacao

def listar_opcoes():
    paginacao(ListaOpcoes())
