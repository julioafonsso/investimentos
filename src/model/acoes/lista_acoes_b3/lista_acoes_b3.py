from urllib.request import urlopen, Request

from bs4 import BeautifulSoup
from simple_term_menu import TerminalMenu

import util.util
from model.acoes.lista_acoes_b3.Acao import Acao
from model.lista import Lista


class ListaAcoesB3(Lista):

    def __init__(self):
        self.__acoes = []
        self.__acoes_filtradas = []
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
        reg_url = "https://fundamentus.com.br/resultado.php"
        req = Request(url=reg_url, headers=headers)
        html = urlopen(req).read()
        bs = BeautifulSoup(html, 'html.parser')
        for linha in bs.findAll('tbody')[0].findChildren("tr"):
            self.__acoes.append(Acao(linha))

        self.__acoes = [x for x in self.__acoes if x.is_valida()]
        self.__acoes_filtradas = self.__acoes

    def get_lista(self) -> []:
        return self.__acoes_filtradas

    def cabecalho(self):
        return "Codigo".rjust(10) + "|" + \
               "Cotação".rjust(12) + "|" + \
               "P/L".rjust(12) + "|" + \
               "P/V".rjust(6) + "|" + \
               "Div. Yield".rjust(12) + "|" + \
               "Crescimento".rjust(12) + "|" + \
               "Margem Liq".rjust(12) + "|" + \
               "Margem Ebit".rjust(12) + "|" + \
               "ROE".rjust(10) + "|" + \
               "ROIC".rjust(10) + "|" + \
               "Tem Opção ?".rjust(12) + "|"

    def filtrar(self):
        indexs = TerminalMenu([
            'P/L',
            'P/V',
            'Div. Yield',
            'Crescimento',
            'Margem EBIT',
            'ROE',
            'Tem Opcão?',

        ], multi_select=True, ).show()

        functions = [self.__filtrar_pl,
                     self.__filtrar_pv,
                     self.__filtrar_dividendo,
                     self.__filtrar_crescimento,
                     self.__filtrar_margem_ebit,
                     self.__filtrar_roe,
                     self.__filtar_acao_com_opcao
                     ]

        for intex in indexs:
            functions[intex]()

    def __filtrar_pl(self):
        util.util.clean()
        valor = util.util.captura_inteiro("Digite o valor maximo do PL")

        tmp = [x for x in self.__acoes_filtradas if x.preco_por_lucro() <= valor]
        self.__acoes_filtradas = tmp

    def __filtrar_pv(self):
        util.util.clean()
        valor = util.util.captura_inteiro("Digite o valor maximo do PV")

        tmp = [x for x in self.__acoes_filtradas if x.preco_por_valor_patrimonial() <= valor]
        self.__acoes_filtradas = tmp

    def __filtrar_dividendo(self):
        util.util.clean()
        valor = util.util.captura_inteiro("Digite o valor minimo do dividendo yield.")

        tmp = [x for x in self.__acoes_filtradas if x.dividendo_yield() >= valor]
        self.__acoes_filtradas = tmp

    def __filtrar_crescimento(self):
        util.util.clean()
        valor = util.util.captura_inteiro("Digite o valor minimo de crescimento.")

        tmp = [x for x in self.__acoes_filtradas if x.crescimento() >= valor]
        self.__acoes_filtradas = tmp

    def __filtrar_margem_ebit(self):
        util.util.clean()
        valor = util.util.captura_inteiro("Digite o valor minimo de margem ebit.")

        tmp = [x for x in self.__acoes_filtradas if x.margem_ebit() >= valor]
        self.__acoes_filtradas = tmp

    def __filtrar_roe(self):
        util.util.clean()
        valor = util.util.captura_inteiro("Digite o valor minimo de ROE.")

        tmp = [x for x in self.__acoes_filtradas if x.roe() >= valor]
        self.__acoes_filtradas = tmp

    def __filtar_acao_com_opcao(self):
        tmp = [x for x in self.__acoes_filtradas if x.tem_opcao()]
        self.__acoes_filtradas = tmp

    def limpar_filtro(self):
        self.__acoes_filtradas = self.__acoes

    def ordernar(self):
        index = TerminalMenu([
            'Codigo Acao',
            'P/L',
            'P/V',
            'Div. Yield',
            'Crescimento',
            'Margem Liq',
            'ROE',
        ]).show()

        match index:
            case 0:
                self.__acoes_filtradas.sort(key=lambda x: x.codigo_acao())
            case 1:
                self.__acoes_filtradas.sort(key=lambda x: x.preco_por_lucro())
            case 2:
                self.__acoes_filtradas.sort(key=lambda x: x.preco_por_valor_patrimonial())
            case 3:
                self.__acoes_filtradas.sort(key=lambda x: x.dividendo_yield(), reverse=True)
            case 4:
                self.__acoes_filtradas.sort(key=lambda x: x.crescimento(), reverse=True)
            case 5:
                self.__acoes_filtradas.sort(key=lambda x: x.margem_liquida(), reverse=True)
            case 6:
                self.__acoes_filtradas.sort(key=lambda x: x.roe(), reverse=True)
