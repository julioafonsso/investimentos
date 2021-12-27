import concurrent.futures

from util.util import clean


def load_objetos_paralelos(lista_parametros, function):
    lista_retorno = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = []
        print("Load... ")
        quantidade_itens = len(lista_parametros)
        quantidade_carregadas = 0
        for parametro in lista_parametros:
            futures.append(executor.submit(function, parametro))

        for future in concurrent.futures.as_completed(futures):
            quantidade_carregadas += 1
            percentual = (quantidade_carregadas / quantidade_itens) * 100
            clean()
            print("Load... " + "{:,.2f}".format(percentual) + "% carregado")
            lista_retorno.append(future.result())

    return lista_retorno
