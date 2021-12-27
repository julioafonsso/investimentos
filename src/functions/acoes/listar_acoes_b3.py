from model.acoes.lista_acoes_b3.lista_acoes_b3 import ListaAcoesB3
from util.paginacao import paginacao

def listar_acoes():
    paginacao(ListaAcoesB3())
