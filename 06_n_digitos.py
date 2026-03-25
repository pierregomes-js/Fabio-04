def main():
    n = int(input('digite um número: '))
    casas = 10
    digitos = 1
    while n <= casas:
        casas *= 10
        digitos += 1
        
    print(f'O número {n} possui {digitos} dígitos. ')


main()