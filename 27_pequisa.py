def main():
    entrevistados = 0
    idade_mulheres = 0
    idade_homens = 0
    homens_solteiros = 0
    mulheres_solteiras = 0
    mulheres_divorciadas = 0
    outros = 0
    mulheres_divorciadas_30 = 0
    mulheres = 0
    homens = 0
    total = idade_mulheres + idade_homens


    sexo = int(input('Sexo(1 - Masculino, 2 - Feminino): '))
    if sexo == 1:

        homens += 1
        idade_homens = int(input('Idade do homem: '))
        estado_civil = int(input('Estado civil(1 : casado, 2 : solteiro, 3: divorciado, 4: viúvo): '))

        if estado_civil == 2:
            homens_solteiros += 1
        else:
            outros += 1
    else:

        mulheres += 1
        idade_mulheres = int(input('Idade da mulher: '))
        estado_civil = int(input('Estado civil(1 : casada, 2 : solteira, 3: divorciada, 4: viúva): '))
        if estado_civil == 2:
            mulheres_solteiras += 1
        elif estado_civil == 3:
            mulheres_divorciadas += 1
        else:
            outros += 1
        
        if idade_mulheres > 30 and estado_civil == 3:
            mulheres_divorciadas_30



    while entrevistados < 10:
        entrevistados += 1

        sexo = int(input('Sexo(1 - Masculino, 2 - Feminino): '))
    if sexo == 1:

        homens += 1
        idade_homens += int(input('Idade do homem: '))
        estado_civil = int(input('Estado civil(1 : casado, 2 : solteiro, 3: divorciado, 4: viúvo): '))

        if estado_civil == 2:
            homens_solteiros += 1
        else:
            outros += 1
    else:

        mulheres += 1
        idade_mulheres += int(input('Idade da mulher: '))
        estado_civil = int(input('Estado civil(1 : casada, 2 : solteira, 3: divorciada, 4: viúva): '))
        if estado_civil == 2:
            mulheres_solteiras += 1
        elif estado_civil == 3:
            mulheres_divorciadas += 1
        else:
            outros += 1
        
        if idade_mulheres > 30 and estado_civil == 3:
            mulheres_divorciadas_30 += 1

    print('Resultado: ')
    print(f'Média das idades das mulheres:')
    print(f'Média das idades dos homens:')
    print(f'Percentual de homens solteiros:')
    print(f'Percentual de mulheres solteiras:')


main()