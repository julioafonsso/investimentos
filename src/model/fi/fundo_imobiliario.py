import bs4

from util.util import converte_string_para_float


class FundoImobiliario:

    def __init__(self, dados: bs4.element.Tag):
        valores = dados.findChildren('td')

        self.__codigo = valores[0].text
        self.__segmento = valores[1].text
        self.__cotacao = converte_string_para_float(valores[2].text)
        self.__ffo_yield = converte_string_para_float(valores[3].text)
        self.__dividendo_yield = converte_string_para_float(valores[4].text)
        self.__preco_por_valor_patrimonial = converte_string_para_float(valores[5].text)
        self.__valor_mercado = converte_string_para_float(valores[6].text)
        self.__liquidez = converte_string_para_float(valores[7].text)
        self.__quantidade_imoveis = int(valores[8].text)
        self.__preco_metro_quadrado = converte_string_para_float(valores[9].text)
        self.__aluguel_metro_quadrado = converte_string_para_float(valores[10].text)
        self.__cap_rate = converte_string_para_float(valores[11].text)
        self.__vacancia = converte_string_para_float(valores[12].text)
        self.__rank = 0

    def is_valida(self):
        return self.__liquidez > 20000 and self.__preco_por_valor_patrimonial > 0 and self.__dividendo_yield > 0

    def print(self):
        return str(self.__codigo).rjust(10) + "|" + \
               str(self.__segmento).rjust(25) + "|" + \
               "R$ {:,.2f}".format(self.__cotacao).rjust(12) + "|" + \
               "{:,.2f}%".format(self.__ffo_yield).rjust(12) + "|" + \
               "{:,.2f}%".format(self.__dividendo_yield).rjust(12) + "|" + \
               "{:,.2f}".format(self.__preco_por_valor_patrimonial).rjust(12) + "|" + \
               "{:,.2f}%".format(self.__cap_rate).rjust(12) + "|" + \
               "{:,.2f}%".format(self.__vacancia).rjust(12) + "|" + \
               str(self.__quantidade_imoveis).rjust(20) + "|" 

    def codigo(self) -> str:
        return self.__codigo

    def segmento(self) -> str:
        return self.__segmento

    def cotacao(self) -> float:
        return self.__cotacao

    def ffo_yield(self) -> float:
        return self.__ffo_yield

    def dividendo_yield(self) -> float:
        return self.__dividendo_yield

    def preco_por_valor_patrimonial(self) -> float:
        return self.__preco_por_valor_patrimonial

    def valor_mercado(self) -> float:
        return self.__valor_mercado

    def liquidez(self) -> float:
        return self.__liquidez

    def quantidade_imoveis(self) -> int:
        return self.__quantidade_imoveis

    def preco_metro_quadrado(self) -> float:
        return self.__preco_metro_quadrado

    def aluguel_metro_quadrado(self) -> float:
        return self.__aluguel_metro_quadrado

    def cap_rate(self) -> float:
        return self.__cap_rate

    def vacancia(self) -> float:
        return self.__vacancia

    def dividendo_yield_mult_pv(self):
        return self.preco_por_valor_patrimonial() * self.dividendo_yield()

    def rank(self):
        return self.__rank

    def set_rank(self, value):
        self.__rank = value