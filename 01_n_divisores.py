def main():
    n = int(input('Digite um número (FLAG = 0): '))
    divisores(n)

    while n != 0:
        n = int(input('Digite um número (FLAG = 0): '))
        divisores(n)

    def divisores(n):
        divisor = n

        while divisor > 0:
            if n % divisor == 0:
                return divisor
            divisor -= 1


main()