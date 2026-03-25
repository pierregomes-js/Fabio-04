def main():
    somatorio = 0
    n1 = int(input('Digite um número inteiro: '))
    n2 = int(input('Digite outro número inteiro: '))
    somatorio = 1

    while somatorio != n2:
        n1 += n1
        somatorio += 1

    print(f'{n2} * {n1 / somatorio} = {n1}')

main()