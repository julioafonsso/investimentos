
from util.util import fim_funcao
from yahoo_fin.stock_info import get_stats

def get_info():
    print("Digite o codigo do ativo.")
    try:
        codigo = input()

        dados = get_stats(codigo.upper())

        print(dados)
    except:
        print("Ação Não Encontrada")

    fim_funcao()
