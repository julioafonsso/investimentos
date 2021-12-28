import bs4

from util.opcoes_ibovespa import load_lista_acoes_com_opcoes
from util.util import converte_string_para_float


class Acao:
    def __init__(self, dados: bs4.element.Tag):
        valores = dados.findChildren('td')

        self.__codigo = valores[0].text
        self.__cotacao = converte_string_para_float(valores[1].text)
        self.__preco_por_lucro = converte_string_para_float(valores[2].text)
        self.__preco_por_valor_patrimonial = converte_string_para_float(valores[3].text)
        self.__psr = converte_string_para_float(valores[4].text)
        self.__div_yield = converte_string_para_float(valores[5].text)
        self.__preco_por_ativo = converte_string_para_float(valores[6].text)
        self.__preco_por_capital_giro = converte_string_para_float(valores[7].text)
        self.__preco_por_ebit = converte_string_para_float(valores[8].text)
        self.__preco_por_ativo_circulante = converte_string_para_float(valores[9].text)
        self.__ev_ebit = converte_string_para_float(valores[10].text)
        self.__ev_ebitda = converte_string_para_float(valores[11].text)
        self.__margem_ebit = converte_string_para_float(valores[12].text)
        self.__margem_liquida = converte_string_para_float(valores[13].text)
        self.__liquidez_corrente = converte_string_para_float(valores[14].text)
        self.__roic = converte_string_para_float(valores[15].text)
        self.__roe = converte_string_para_float(valores[16].text)
        self.__liquidez = converte_string_para_float(valores[17].text)
        self.__patrimonio_liquido = converte_string_para_float(valores[18].text)
        self.__divida_liquida_por_patrimonio = converte_string_para_float(valores[19].text)
        self.__crescimento = converte_string_para_float(valores[20].text)
        self.__tem_opcao = self.__codigo in load_lista_acoes_com_opcoes()

    def print(self):
        return str(self.__codigo).rjust(10) + "|" + \
               "R$ {:,.2f}".format(self.__cotacao).rjust(12) + "|" + \
               "{:,.2f}".format(self.__preco_por_lucro).rjust(12) + "|" + \
               "{:,.2f}".format(self.__preco_por_valor_patrimonial).rjust(6) + "|" + \
               "{:,.2f}%".format(self.__div_yield).rjust(12) + "|" + \
               "{:,.2f}%".format(self.__crescimento).rjust(12) + "|" + \
               "{:,.2f}%".format(self.__margem_liquida).rjust(12) + "|" + \
               "{:,.2f}%".format(self.__margem_ebit).rjust(12) + "|" + \
               "{:,.2f}%".format(self.__roe).rjust(10) + "|" + \
               "{:,.2f}%".format(self.__roic).rjust(10) + "|" + \
               str(self.__tem_opcao).rjust(12) + "|"

    def is_valida(self):
        return self.__liquidez > 0 and \
               self.__preco_por_lucro > 0 and \
               self.__preco_por_valor_patrimonial > 0

    def preco_por_lucro(self) -> float:
        return self.__preco_por_lucro

    def preco_por_valor_patrimonial(self) -> float:
        return self.__preco_por_valor_patrimonial

    def dividendo_yield(self) -> float:
        return self.__div_yield

    def crescimento(self) -> float:
        return self.__crescimento

    def margem_liquida(self) -> float:
        return self.__margem_liquida

    def margem_ebit(self) -> float:
        return self.__margem_ebit

    def roe(self) -> float:
        return self.__roe

    def codigo_acao(self) -> str:
        return self.__codigo

    def tem_opcao(self) -> bool:
        return self.__tem_opcao
