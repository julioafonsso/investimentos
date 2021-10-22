from yahoo_fin.stock_info import tickers_nasdaq

from util.paginacao import paginacao


def listar_ativos_nasdaq():

    ativos = tickers_nasdaq(True)

    cabecalho = "Codigo".ljust(10) + " | " + "Nome"

    ativosFormatados = []

    for ativo in ativos.values:
        linha = ativo[0].ljust(10) + " | " + \
                str(ativo[1])[0:100]
        ativosFormatados.append(linha)

    paginacao(ativosFormatados, cabecalho)
