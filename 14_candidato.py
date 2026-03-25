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

    print('Resultado:')
    print(f'Percentual da candidata Dilma: {((dilma / total) * 100):.2f}%.')
    print(f'Percentual do candidato Serra: {((serra / total) * 100):.2f}%.')
    print(f'Percentual do candidato Ciro Gomes: {((cirogomes / total) * 100):.2f}%.')
    print(f'Percentual de outros candidatos: {((outros_candidatos / total) * 100):.2f}%.')
    print(f'Percentual de indecisos: {((indecisos / total) * 100):.2f}%.')
    print(f'Percentual de votos nulo/branco: {((nulo_branco / total) * 100):.2f}%.')
    print(f'Total de entrevistados: {total}.')

main()
#incompleto