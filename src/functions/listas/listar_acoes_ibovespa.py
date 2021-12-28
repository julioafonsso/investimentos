from model.acoes.ibovespa.lista_acoes_ibovespa import ListaAcoesIbovespa
from util.paginacao import paginacao

def listar_acoes_ibovespa():
    paginacao(ListaAcoesIbovespa())
