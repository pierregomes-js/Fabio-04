def main():
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))
    mdc = 1

    while n1 != 1 or n2 != 2:
        if n1 % 2 == 0 and n2 % 2 == 0:
            mdc *= 2
            n1 /= 2
            n2 /= 2
        elif n1 % 3 == 0 and n2 % 3 == 0:
            mdc *= 3
            n1 /= 3
            n2 /= 3
        elif n1 % 5 == 0 and n2 % 5 == 0:
            mdc *= 5
            n1 /= 5
            n2 /= 5
        elif n1 % 7 == 0 and n2 % 7 == 0:
            mdc *= 7
            n1 /= 7
            n2 /= 7

    print(mdc)


main()