def main():
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))
    mmc = 1

    while n1 != 1 and n2 != 1:
        if n1 % 2 == 0 or n2 % 2 == 0:
            mmc *= 2
            if n1  % 2 == 0:
                n1 /= 2
            if n2 % 2 == 0:
                n2 /= 2
        elif n1 % 3 == 0 or n2 % 3 == 0:
            mmc *= 3
            if n1  % 3 == 0:
                n1 /= 3
            if n2 % 3 == 0:
                n2 /= 3
        elif n1 % 5 == 0 or n2 % 5 == 0:
            mmc *= 5
            if n1 % 5 == 0:
                n1 /= 5
            if n2 % 5 == 0:
                n2 /= 5
        elif n1 % 7 == 0 or n2 % 7 == 0:
            mmc *= 7
            if n1  % 7 == 0:
                n1 /= 7
            if n2 % 7 == 0:
                n2 /= 7

    print(mmc)


main()