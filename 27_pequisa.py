def main():
    homens_solteiros = 0
    outros = 0
    mulheres_solteiras = 0
    mulheres_divorciadas_30 = 0
    idade_mulheres = 0
    idade_homens = 0
    mulheres = 0
    homens = 0
    
    sexo = int(input('Sexo(1 - Masculino, 2 - Feminino): '))
    idade = int(input('Idade: '))
    estado_civil = int(input('Estado civil(1 : casado, 2 : solteiro, 3: divorciado, 4: viúvo): '))
    
    
    while (mulheres + homens) <= 100:
        if sexo == 1:
            homens += 1
            idade_homens += idade
            if estado_civil == 2:
                homens_solteiros += 1
            else:
                outros += 1
                
        if sexo == 2:
            mulheres += 1
            idade_mulheres += idade
            if estado_civil == 2:
                mulheres_solteiras += 1
            elif estado_civil == 3 and idade > 30:
                mulheres_divorciadas_30 += 1
            else:
                outros += 1
        
        sexo = int(input('Sexo(1 - Masculino, 2 - Feminino): '))
        idade = int(input('Idade: '))
        estado_civil = int(input('Estado civil(1 : casado, 2 : solteiro, 3: divorciado, 4: viúvo): '))
    total = mulheres + homens
    print('Resultado da pesquisa: ')
    print(f'Média das idades das mulheres: {(idade_mulheres / mulheres):.2f}.')
    print(f'Média das idades dos homens: {(idade_homens / homens):.2f}.')
    print(f'Percentual de homens solteiros: {((homens_solteiros / total)* 100):.2f}%.' )
    print(f'Percentual de mulheres solteiras: {((mulheres_solteiras / total)*100):.2f}%.')
    print(f'Quantidade de mulheres divorciadas acima de 30 anos: {mulheres_divorciadas_30}.')