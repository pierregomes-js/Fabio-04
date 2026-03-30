def main():
    primeiro_numero = int(input('Digite um número: '))
    numeros = int(input('Digite outro número:'))

    while numeros != primeiro_numero:
        numeros = int(input('Digite outro número:'))

    print('Você repetiu um número.')

main()