from yahoo_fin.stock_info import tickers_ibovespa

from util.paginacao import paginacao


def listarAtivosIbovespa():

    cabecalho = "Codigo".ljust(10) + " | " + "Nome".ljust(15) + " | " + "Setor".ljust(50) + " | " + "Site"

    ativos = tickers_ibovespa(True)
    ativosFormatados = []
    for ativo in ativos.values:
        linha = ativo[0].ljust(10) + " | " + \
                ativo[1].ljust(15) + " | " + \
                ativo[2][0:50].ljust(50) + " | " + \
                ativo[4]
        ativosFormatados.append(linha)

    paginacao(ativosFormatados, cabecalho)

