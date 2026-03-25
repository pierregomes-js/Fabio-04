def main():
    soma_salarios = 0
    soma_reajuste = 0
    salario = float(input('Insira o salário do funcionário (FLAG = 0): '))

    while salario != 0:

        soma_salarios += salario

        if salario <= 2999.99:
            salario = salario * 1.25
            soma_reajuste += salario
        elif salario <= 5999.99:
            salario = salario * 1.20
            soma_reajuste += salario
        elif salario <= 9999.99:
            salario = salario * 1.15
            soma_reajuste += salario
        else:
            salario = salario * 1.10
            soma_reajuste += salario

        salario = float(input('Insira o salário do funcionário (FLAG = 0): '))

    print('Resultado: ')
    print(f'Soma dos salarios atuais = {soma_salarios:.2f} R$.')
    print(f'Soma dos salarios reajustados = {soma_reajuste:.2f} R$.')
    print(f'Diferença dos somatórios dos salários atuais com os reajustados = {(soma_reajuste - soma_salarios):.2f} R$.')

main()