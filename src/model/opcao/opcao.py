from enum import Enum

from getch import getch


class TipoOpcao(Enum):
    CALL = 'calls'
    PUT = 'puts'


class Opcao:

    def __init__(self,
                 codigo_acao,
                 valor_acao,
                 data_ultima_negociacao_acao,
                 data_vencimento,
                 tipo:TipoOpcao,
                 dados):
        self.__data_vencimento = data_vencimento
        self.__tipo = tipo.value
        self.__ticket = codigo_acao[0:4] + dados[0]
        self.__ind_formador_mercado = dados[1] == "1"
        self.__modelo = "Americana" if dados[2] == "A" else "Europeia"
        self.__striker = float(dados[3])
        self.__ultimo_preco = 0 if str(dados[5]) == 'None' else float(dados[5])
        self.__ultima_data_negociada = dados[7]
        self.__volatilidade = 0 if str(dados[10]) == 'None' else float(dados[10])
        self.__delta = 0 if str(dados[11]) == 'None' else float(dados[11])
        self.__valor_acao = valor_acao
        self.__data_ultima_negociacao_acao = data_ultima_negociacao_acao
        self.__codigo_acao = codigo_acao

    def print(self):
        return str(self.__ticket).rjust(10) + "|" + \
               str(self.__tipo).rjust(6) + "|" + \
               str(self.__data_vencimento).rjust(12) + "|" + \
               "R$ {:,.2f}".format(self.__valor_acao).rjust(12) + "|" + \
               "R$ {:,.2f}".format(self.__striker).rjust(10) + "|" + \
               "R$ {:,.2f}".format(self.preco_medio_final()).rjust(9) + "|" + \
               "R$ {:,.2f}".format(self.__ultimo_preco).rjust(8) + "|" + \
               "R$ {:,.2f}".format(self.valor_intriseco()).rjust(10) + "|" + \
               "R$ {:,.2f}".format(self.valor_extrinseco()).rjust(11) + "|" + \
               "{:,.2f} %".format(self.percentual_lucro()).rjust(7) + "|" + \
               "{:,.2f} %".format(self.percentual_lucro_valor_intriseco()).rjust(10) + "|" + \
               "{:,.2f} %".format(self.percentual_lucro_valor_extrinseco()).rjust(11) + "|" + \
               "{:,.2f} %".format(self.diferenca_preco()).rjust(14) + "|" + \
               "{:,.2f} %".format(self.diferenca_preco_medio_final()).rjust(14) + "|" + \
               str(self.__delta).rjust(10) + "|"

    def striker(self):
        return self.__striker

    def ultima_data_negociada(self):
        return self.__ultima_data_negociada

    def ultimo_preco(self):
        return self.__ultimo_preco

    def diferenca_preco_abs(self):
        return abs(self.diferenca_preco())

    def diferenca_preco(self):
        return (self.__striker * 100 / self.__valor_acao) - 100

    def diferenca_preco_medio_final(self):
        return (self.preco_medio_final() * 100 / self.__valor_acao) - 100

    def preco_medio_final(self):
        if self.is_call():
            return self.__striker + self.__ultimo_preco
        else:
            return self.__striker - self.__ultimo_preco

    def valor_intriseco(self):
        if self.__ultimo_preco == 0:
            return 0

        if self.is_call():
            if self.__valor_acao > self.__striker:
                return self.__valor_acao - self.__striker
        else:
            if self.__striker > self.__valor_acao:
                return self.__striker - self.__valor_acao
        return 0

    def valor_extrinseco(self):
        return self.__ultimo_preco - self.valor_intriseco()

    def percentual_lucro_valor_intriseco(self):
        return 0 if self.__ultimo_preco == 0 else self.valor_intriseco() / self.__striker * 100

    def percentual_lucro_valor_extrinseco(self):
        return 0 if self.__ultimo_preco == 0 else self.valor_extrinseco() / self.__striker * 100

    def percentual_lucro(self):
        return 0 if self.__ultimo_preco == 0 else self.__ultimo_preco / self.__striker * 100

    def delta(self):
        return abs(self.__delta)

    def is_call(self):
        return self.__tipo == TipoOpcao.CALL.value

    def tipo(self):
        return self.__tipo

    def is_valida(self):
        return self.ultimo_preco() > 0 and \
               self.diferenca_preco_abs() < 20 and \
               self.ultima_data_negociada() == self.__data_ultima_negociacao_acao and \
               self.delta() != 0
    
    def codigo_acao(self):
        return self.__codigo_acao

    def data_vencimento(self):
        return self.__data_vencimento
