def main():
    x = float(input('Digite um número(X): '))
    n = float(input('Digite um número(N): '))

    while n != 2:
        x = x / n
        n -= 1
        print(f'{x:.2f}')

main()