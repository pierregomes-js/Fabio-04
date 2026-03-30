def main():
    ano = 1
    meses = ano * 12
    valor_mensal = float(input('Valor investido por mês: '))
    taxa_mensal = float(input('Taxa de juros mensal em %: '))
    taxa_mensal = taxa_mensal / 100

    def saldo_total(valor_mensal, taxa_mensal, meses):
        mes_atual = 1
        saldo = 0

        while mes_atual <= meses:
            meses_restantes = meses - mes_atual
            montante = valor_mensal * ((1 + taxa_mensal) ** meses_restantes)
            mes_atual += 1
            saldo += montante

        return saldo
    
    saldo = saldo_total(valor_mensal, taxa_mensal, meses)
    print(f'Saldo do investimento após 1 ano: {saldo:.2f}.')
    continuar = input('Deseja processar mais um ano (S/N) ?')

    while continuar == 'S':
        ano += 1
        meses = ano * 12
        saldo = saldo_total(valor_mensal, taxa_mensal, meses)

        
        print(f'Saldo do investimento após {ano} anos: {saldo:.2f}.')
        continuar = input('Deseja processar mais um ano (S/N) ?')



main()