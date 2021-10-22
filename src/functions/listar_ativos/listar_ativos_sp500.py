from yahoo_fin.stock_info import tickers_sp500

from util.paginacao import paginacao


def listar_ativos_sp500():

    ativos = tickers_sp500(True)

    cabecalho = "Codigo".ljust(10) + " | " + "Nome".ljust(30) + " | " + "Setor".ljust(50)

    ativosFormatados = []

    for ativo in ativos.values:
        linha = ativo[0].ljust(10) + " | " + \
                ativo[1].ljust(30) + " | " + \
                ativo[4][0:50].ljust(50)
        ativosFormatados.append(linha)

    paginacao(ativosFormatados, cabecalho)


