def main():
    entrevistados = 0
    idade_mulheres = 0
    idade_homens = 0
    homens_solteiros = 0
    mulheres_solteiras = 0
    mulheres_divorciadas = 0
    outros = 0
    total = idade_mulheres + idade_homens


    sexo = int(input('Sexo(1 - Masculino, 2 - Feminino): '))
    if sexo == 1:
        idade_homens = int(input('Idade do homem: '))
        estado_civil = int(input('Estado civil(1 : casado, 2 : solteiro, 3: divorciado, 4: viúvo): '))
    else:
        idade_mulheres = int(input('Idade da mulher: '))
        estado_civil = int(input('Estado civil(1 : casado, 2 : solteiro, 3: divorciado, 4: viúvo): '))

    while entrevistados < 100:
        entrevistados += 1

def civil_mulheres(e, s, d, o, i):
    if e 

def civil_homens(e, s, o):
    ...

main()