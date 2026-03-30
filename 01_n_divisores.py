def main():

    def obter_divisores(n):
        print(f'Divisores de {n}: ')
        divisor = 1

        while divisor <= n:
            if n % divisor == 0:
                print(divisor, end=' ')
            divisor += 1
        return
    
    numero = int(input('Insira um número(flag = 0): '))

    while numero != 0:
        obter_divisores(numero)
        print(' ')
        numero = int(input('Insira um número(flag = 0): '))

main()