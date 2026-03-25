def main():
    print('Questionário do filme')

    quantidade_regular = 0
    quantidade_bom = 0
    quantidade_otimo = 0

    idade = int(input('Idade do espectador:(FLAG = -1) '))
    opniao = int(input('Opnião ao filme(1 = ótimo , 2 = bom, 3 = regular, 4 = péssimo) : '))
    quantidade_pessoas = 1
    idade_somatorio = 0
    quantidade_otimo = 0

    if opniao == 3:
        quantidade_regular += 1
    elif opniao == 2:
        quantidade_bom += 1
    elif opniao == 1:
        idade_somatorio += idade
        quantidade_otimo += 1


    while idade != -1:
        quantidade_pessoas += 1
        idade = int(input('Idade do espectador:(FLAG = -1) '))
        if idade == -1:
            break
        else: 
            opniao = int(input('Opnião ao filme(1 = ótimo , 2 = bom, 3 = regular, 4 = péssimo) : '))

            if opniao == 3:
                quantidade_regular += 1
            elif opniao == 2:
                quantidade_bom += 1
            elif opniao == 1:
                idade_somatorio += idade
                quantidade_otimo += 1
    

    print(f'Média das idades das pessoas que responderam ótimo: {(idade_somatorio / quantidade_otimo):.2f}.')
    print(f'Quantidade de pessoas que responderam regular: {quantidade_regular}')
    print(f'Percentual de pessoas que responderam bom : {((quantidade_bom / quantidade_pessoas) * 100):.2f}%.')




main()