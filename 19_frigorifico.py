def main():
    print('Frigorífico.')

    print('Cartão 1: ')
    codigo = int(input('Código de identificação do boi(flag = 0): '))
    peso = float(input('Peso do boi: '))

    cartao = 1

    codigo_gordo = codigo
    codigo_magro = codigo
    peso_gordo = peso
    peso_magro = peso

    while codigo != 0:
        cartao += 1
        if peso > peso_gordo:
            codigo_gordo = codigo
            peso_gordo = peso
        if peso < peso_magro:
            codigo_magro = codigo
            peso_magro = peso

        print(f'Cartão {cartao}:')
        codigo = int(input('Código de identificação do boi(flag = 0): '))
        if codigo == 0:
            break
        peso = float(input('Peso do boi: '))
    
    print('Resultado final:')
    print(f'Código do boi mais gordo e seu peso: {codigo_gordo}, {peso_gordo} kg.')
    print(f'Código do boi mais magro e seu peso: {codigo_magro}, {peso_magro} kg.')


main()