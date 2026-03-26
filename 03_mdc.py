def main():
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))
    mdc = 2

    while n1 % mdc == 0 or n2 % mdc == 0:
        n1 /= mdc
        n2 /= mdc
        mdc += 1
        print(f'{n1}, {n2}')

main()