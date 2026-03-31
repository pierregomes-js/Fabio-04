def main():
    print('Pesquisa eleitoral')

    serra = 0
    dilma = 0
    cirogomes = 0

    outros_candidatos = 0
    indecisos = 0
    nulo_branco = 0
    print('Serra = 45 \nDilma = 13 \nCiro Gomes = 23 \nindeciso = 99, \noutros = 98, \nnulo/branco = 0.')
    opniao = int(input('Opnião de voto (FLAG = -1): '))

    while opniao != -1:


        if opniao == 45:
            serra += 1
        elif opniao == 13:
            dilma += 1
        elif opniao == 23:
            cirogomes += 1
        elif opniao == 99:
            indecisos += 1
        elif opniao == 98:
            outros_candidatos += 1
        elif opniao == 0:
            nulo_branco += 1

        opniao = int(input('Opnião de voto (FLAG = -1): '))

    total = serra + dilma + cirogomes + outros_candidatos + indecisos + nulo_branco

    def percentual(candidato, total):
        return f'{((candidato / total) * 100):.2f}%'
    
    percentual_dilma = percentual(dilma, total)
    percentual_serra = percentual(serra, total)
    percentual_cirogomes = percentual(cirogomes, total)
    percentual_outros = percentual(outros_candidatos, total)
    percentual_indecisos = percentual(indecisos, total)
    percentual_nulobranco = percentual(nulo_branco, total)


    print('Resultado:')
    print(f'Percentual da candidata Dilma: {percentual_dilma}.')
    print(f'Percentual do candidato Serra: {percentual_serra}.')
    print(f'Percentual do candidato Ciro Gomes: {percentual_cirogomes}.')
    print(f'Percentual de outros candidatos: {percentual_outros}.')
    print(f'Percentual de indecisos: {percentual_indecisos}.')
    print(f'Percentual de votos nulo/branco: {percentual_nulobranco}.')
    print(f'Total de entrevistados: {total}.')

    if ((dilma / total) * 100) <= 50 and ((serra / total) * 100) <= 50 and ((cirogomes / total) * 100) <= 50:
        print('Será previsto um segundo turno.')
    else:
        print('Não haverá segundo turno.')


main()