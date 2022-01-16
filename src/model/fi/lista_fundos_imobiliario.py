from urllib.request import urlopen, Request

from bs4 import BeautifulSoup
from simple_term_menu import TerminalMenu

import util.util
from model.fi.fundo_imobiliario import FundoImobiliario
from model.lista import Lista


class ListaFundoImobiliario(Lista):

    def __init__(self):
        self.__fundos = []
        self.__fundos_filtrados = []

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
        reg_url = "https://fundamentus.com.br/fii_resultado.php"
        req = Request(url=reg_url, headers=headers)
        html = urlopen(req).read()
        bs = BeautifulSoup(html, 'html.parser')

        for linha in bs.findAll('tbody')[0].findChildren("tr"):
            self.__fundos.append(FundoImobiliario(linha))

        self.__fundos = [x for x in self.__fundos if x.is_valida()]

        self.__fundos_filtrados = self.__fundos

    def cabecalho(self) -> str:
        return "Codigo".rjust(10) + "|" + \
               "Segmento".rjust(25) + "|" + \
               "Cotação".rjust(12) + "|" + \
               "FFO Yield".rjust(12) + "|" + \
               "Div. Yield".rjust(12) + "|" + \
               "P/V".rjust(12) + "|" + \
               "CAP Rate".rjust(12) + "|" + \
               "Vacancia".rjust(12) + "|" + \
               "Quantidade Imoveis".rjust(20) + "|"

    def get_lista(self) -> []:
        return self.__fundos_filtrados

    def ordernar(self):
        index = TerminalMenu([
            'Codigo',
            'Segmento',
            'Dividendo Yield',
            'P/V',
            'Cap Rate',
            'Rank Dividendo Yield e PV'
        ]).show()

        match index:
            case 0:
                self.__fundos_filtrados.sort(key=lambda x: x.codigo())
            case 1:
                self.__fundos_filtrados.sort(key=lambda x: x.segmento())
            case 2:
                self.__fundos_filtrados.sort(key=lambda x: x.dividendo_yield(), reverse=True)
            case 3:
                self.__fundos_filtrados.sort(key=lambda x: x.preco_por_valor_patrimonial())
            case 4:
                self.__fundos_filtrados.sort(key=lambda x: x.cap_rate(), reverse=True)
            case 5:
                self.__ordernar_rank()

    def filtrar(self):
        indexs = TerminalMenu([
            'Dividendo Yield',
            'P/V',
            'Cap Rate',
            'Quantidade Imoveis',
            'Segmento',
        ], multi_select=True, ).show()

        functions = [
            self.__filtrar_dividendo,
            self.__filtrar_pv,
            self.__filtrar_cap_rate,
            self.__filtrar_quantidade_imoveis,
            self.__filtrar_segmento
        ]

        for intex in indexs:
            functions[intex]()

    def __filtrar_pv(self):
        util.util.clean()
        valor = util.util.captura_inteiro("Digite o valor maximo do PV")

        tmp = [x for x in self.__fundos_filtrados if x.preco_por_valor_patrimonial() <= valor]
        self.__fundos_filtrados = tmp

    def __filtrar_dividendo(self):
        util.util.clean()
        valor = util.util.captura_inteiro("Digite o valor minimo do dividendo yield.")

        tmp = [x for x in self.__fundos_filtrados if x.dividendo_yield() >= valor]
        self.__fundos_filtrados = tmp

    def __filtrar_cap_rate(self):
        util.util.clean()
        valor = util.util.captura_inteiro("Digite o valor minimo do Cap Rate")

        tmp = [x for x in self.__fundos_filtrados if x.cap_rate() >= valor]
        self.__fundos_filtrados = tmp

    def __filtrar_segmento(self):
        util.util.clean()
        segmentos = []
        [segmentos.append(x.segmento()) for x in self.__fundos_filtrados if x.segmento() not in segmentos and len(x.segmento()) > 0]

        indexs = TerminalMenu(segmentos, multi_select=True ).show()

        segmentos_selecionados = []
        for index in indexs:
            segmentos_selecionados.append(segmentos[index])

        self.__fundos_filtrados = [x for x in self.__fundos_filtrados if x.segmento() in segmentos_selecionados]

    def __filtrar_quantidade_imoveis(self):
        util.util.clean()
        valor = util.util.captura_inteiro("Digite a quantidade minima de imoveis")

        tmp = [x for x in self.__fundos_filtrados if x.quantidade_imoveis() >= valor]
        self.__fundos_filtrados = tmp

    def limpar_filtro(self):
        self.__fundos_filtrados = self.__fundos

    def __ordernar_rank(self):
        self.__fundos_filtrados.sort(key=lambda x: x.dividendo_yield(), reverse=True)

        for index, fundo in  enumerate(self.__fundos_filtrados):
            fundo.set_rank(index)

        self.__fundos_filtrados.sort(key=lambda x: x.preco_por_valor_patrimonial())

        for index, fundo in  enumerate(self.__fundos_filtrados):
            fundo.set_rank(fundo.rank() + index)

        self.__fundos_filtrados.sort(key=lambda x: x.rank())
