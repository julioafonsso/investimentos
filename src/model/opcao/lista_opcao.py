from datetime import datetime

import requests
from simple_term_menu import TerminalMenu

from model.lista import Lista
from model.opcao.opcao import Opcao, TipoOpcao
from util.load_object_paralelo import load_objetos_paralelos
from util.opcoes_ibovespa import load_lista_acoes_com_opcoes


class ListaOpcoes(Lista):

    def __init__(self):
        self.__opcoes = []
        self.__opcoes_filtradas = []
        self.__datas_vencimento = set()

        opcoes = load_objetos_paralelos(load_lista_acoes_com_opcoes(), self.__load_acao)

        for opcao in opcoes:
            self.__set_values(opcao[0], opcao[1])
        self.__opcoes = [x for x in self.__opcoes if x.is_valida()]
        self.__opcoes_filtradas = self.__opcoes

    def __set_values(self, cod_acao, json):
        valor_acao = json['u']
        data_cotacao = json['y']

        self.__datas_vencimento.update([x['dt'] for x in json['expirations']])

        for data in json['expirations']:
            for call in data["calls"]:
                self.__opcoes.append(Opcao(cod_acao, valor_acao, data_cotacao, data["dt"], TipoOpcao.CALL, call))
            for put in data["puts"]:
                self.__opcoes.append(Opcao(cod_acao, valor_acao, data_cotacao, data["dt"], TipoOpcao.PUT, put))

    def __load_acao(self, cod_acao):
        json = requests.get('https://opcoes.net.br/opcoes/bovespa/' + cod_acao + '/json').json()['data']
        return [cod_acao, json]

    def get_lista(self):
        return self.__opcoes_filtradas

    def limpar_filtro(self):
        self.__opcoes_filtradas = self.__opcoes

    def cabecalho(self):
        return "Codigo".rjust(10) + "|" + \
               "Tipo".rjust(6) + "|" + \
               "Vencimento".rjust(12) + "|" + \
               "Preço Açao".rjust(12) + "|" + \
               "Striker".rjust(10) + "|" + \
               "PM Final".rjust(9) + "|" + \
               "Preço".rjust(8) + "|" + \
               "Intriseco".rjust(10) + "|" + \
               "Extrinseco".rjust(11) + "|" + \
               "Lucro".rjust(7) + "|" + \
               "Intriseco".rjust(10) + "|" + \
               "Extrinseco".rjust(11) + "|" + \
               "Diff Preço %".rjust(14) + "|" + \
               "Diff PM %".rjust(14) + "|" + \
               "Delta".rjust(10) + "|"

    def filtrar(self):
        self.limpar_filtro()
        indexs = TerminalMenu([
            'Ação',
            'Tipo',
            'Data',
            'Delta Menor que 50',
            'Delta Menor que 40',
            'Delta Menor que 30',
            'Delta Menor que 20',
            'Delta Menor que 10',
        ], multi_select=True, ).show()

        functions = [self.__filtrar_por_acao,
                     self.__filtrar_por_tipo,
                     self.__filtar_por_data,
                     self.__filtrar_delta_menor_50,
                     self.__filtrar_delta_menor_40,
                     self.__filtrar_delta_menor_30,
                     self.__filtrar_delta_menor_20,
                     self.__filtrar_delta_menor_10
                     ]
        for index in indexs:
            functions[index]()

    def __filtrar_por_acao(self):
        acoes = load_lista_acoes_com_opcoes()
        print(" Selecione a ação")
        acao = acoes[TerminalMenu(acoes).show()]
        tmp = [x for x in self.__opcoes_filtradas if x.codigo_acao() == acao]
        self.__opcoes_filtradas = tmp

    def __filtrar_por_tipo(self):
        tipos = [TipoOpcao.CALL.value, TipoOpcao.PUT.value]
        tipo = tipos[TerminalMenu(tipos).show()]
        tmp = [x for x in self.__opcoes_filtradas if x.tipo() == tipo]
        self.__opcoes_filtradas = tmp

    def __filtar_por_data(self):
        datas = list(self.__datas_vencimento)
        datas.sort()
        data = datas[TerminalMenu(datas).show()]
        tmp = [x for x in self.__opcoes_filtradas if x.data_vencimento() == data]
        self.__opcoes_filtradas = tmp

    def __filtrar_delta_menor(self, valor):
        tmp = [x for x in self.__opcoes_filtradas if abs(x.delta()) < valor]
        self.__opcoes_filtradas = tmp

    def __filtrar_delta_menor_10(self):
        self.__filtrar_delta_menor(0.1)

    def __filtrar_delta_menor_20(self):
        self.__filtrar_delta_menor(0.2)

    def __filtrar_delta_menor_30(self):
        self.__filtrar_delta_menor(0.3)

    def __filtrar_delta_menor_40(self):
        self.__filtrar_delta_menor(0.4)

    def __filtrar_delta_menor_50(self):
        self.__filtrar_delta_menor(0.5)

    def ordernar(self):
        index = TerminalMenu([
            'Ação',
            'Tipo',
            'Data',
            'Preco Medio Final',
            'Percentual Lucro',
            'Percentual Valor Intrinseco',
            'Percentual Valor Extrinseco',
        ]).show()

        match index:
            case 0:
                self.__opcoes_filtradas.sort(key=lambda x: x.codigo_acao())
            case 1:
                self.__opcoes_filtradas.sort(key=lambda x: x.tipo())
            case 2:
                self.__opcoes_filtradas.sort(key=lambda x: x.data_vencimento())
            case 3:
                self.__opcoes_filtradas.sort(key=lambda x: x.preco_medio_final())
            case 4:
                self.__opcoes_filtradas.sort(key=lambda x: x.percentual_lucro(), reverse=True)
            case 5:
                self.__opcoes_filtradas.sort(key=lambda x: x.percentual_lucro_valor_intriseco(), reverse=True)
            case 6:
                self.__opcoes_filtradas.sort(key=lambda x: x.percentual_lucro_valor_extrinseco(), reverse=True)
