from model.fi.lista_fundos_imobiliario import ListaFundoImobiliario
from util.paginacao import paginacao

def listar_fundos_imobiliarios():
    paginacao(ListaFundoImobiliario())
