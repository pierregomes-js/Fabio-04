def main():
    emprestimo = 3000
    parcela = 200
    dia_util = 0

    while parcela < emprestimo:
        parcela = parcela + 200
        emprestimo = emprestimo + (emprestimo * 0.85)
        dia_util += 1
    print(f'Quantidade de dias úteis para realizar o pagamento = {dia_util}')
    print(f'juros = {emprestimo - ((0.85) * dia_util)}')

main()