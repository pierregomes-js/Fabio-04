def main():
    print('Progressão Geométrica')
    primeiro_termo = int(input('Primeiro termo: '))
    razao = int(input('Razão: '))
    n = int(input('Quantidade de termos: '))
    posicao = 0

    while n > 0:
        n -= 1
        posicao += 1
        print(primeiro_termo * (razao ** posicao) )   

main()