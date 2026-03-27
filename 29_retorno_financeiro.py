def main():
    valor_mensal = float(input('Valor investido por mês: '))
    taxa_mensal = float(input('Taxa de juros mensal: '))
    saldo = calculo(valor_mensal, taxa_mensal)
    # somatorio_anos = 0
    # somatorio_saldo = 0
    print(f'Saldo do investimento após 1 ano: {saldo:.2f}R$.')
    # ano = input('Deseja processar mais um ano (S/N)?: ')

    # while ano == 'S':
    #     somatorio_anos += 1
    #     somatorio_saldo += saldo
    #     valor_mensal = 
    #     taxa_mensal =
    #     saldo = retorno_investimento(valor_mensal, taxa_mensal)
    #     ano = input('Deseja processar mais um ano (S/N)?: ')

def calculo(v, t):
    return ((v * 12) * ((100 - t / 100) * 12))


main()