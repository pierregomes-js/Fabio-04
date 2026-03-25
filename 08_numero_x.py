def main():
    somatorio = 0
    x = int(input('Digite um número: '))

    while somatorio != x:
        somatorio = 0
        x = int(input('Digite outro número: '))
        somatorio += x
        x = int(input('Digite outro número: '))
        somatorio += x


main()