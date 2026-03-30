def main():
    clube_a = 0
    clube_b = 0
    qtd_provas = int(input('Digite a quantidade de provas: '))
    qtd_nadadores = int(input('Digite a quantidade de nadadores: '))

    nome_nadador = input('Nome do nadador: ')
    classificacao_nadador = int(input('classificação do nadador: '))
    tempo_nadador = int(input('Tempo do nadador: '))
    clube_nadador = input('Clube do nadador (a ou b): ')

    pontos = calcular_pontos(classificacao_nadador)


    while qtd_provas > 1 and qtd_nadadores > 1:
        qtd_provas -= 1
        qtd_nadadores -=1

        if clube_nadador == 'a':
            clube_a += pontos
        else:
            clube_b += pontos


        print('Próximo nadador: ')
        nome_nadador = input('Nome do nadador: ')
        classificacao_nadador = int(input('classificação do nadador: '))
        tempo_nadador = int(input('Tempo do nadador: '))
        clube_nadador = input('Clube do nadador (a ou b): ')


    print('Resultado da competição:')
    print(f'Pontos do clube A: {clube_a}.')
    print(f'Pontos do clube B: {clube_b}.')
    if clube_b > clube_a:
        print('O clube B foi o vencedor.')
    else:
        print('O clube A foi o vencedor.')


def calcular_pontos(c):
    if c == 1:
        return 9
    elif c == 2:
        return 6
    elif c == 3:
        return 4
    else:
        return 3


main()
#incompleto