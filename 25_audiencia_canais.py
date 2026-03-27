def main():

    canal_2 = 0
    canal_4 = 0
    canal_5 = 0
    canal_7 = 0
    canal_10 = 0
    print('Canais: ')
    print('2 \n4 \n5 \n7 \n10')
    
    canal = int(input('Selecione o canal que deseja assistir(fim = 0): '))
    while canal != 0:
        if canal == 2:
            canal_2 += 1
        elif canal == 4:
            canal_4 += 1
        elif canal == 5:
            canal_5 += 1
        elif canal == 7:
            canal_7 += 1
        else:
            canal_10 += 1
        canal = int(input('Selecione o canal que deseja assistir(fim = 0): '))
        

    total = canal_2 + canal_4 + canal_5 + canal_7 + canal_10

    def percentual(canal, total):
        return (canal / total) * 100
    
    percentual_2 = percentual(canal_2, total)
    percentual_4 = percentual(canal_4, total)
    percentual_5 = percentual(canal_5, total)
    percentual_7 = percentual(canal_7, total)
    percentual_10 = percentual(canal_10, total)

    print('Resultado: ')
    print(f'Percentual da audiência do canal 2: {percentual_2:.2f}%.')
    print(f'Percentual da audiência do canal 4: {percentual_4:.2f}%.')
    print(f'Percentual da audiência do canal 5: {percentual_5:.2f}%.')
    print(f'Percentual da audiência do canal 7: {percentual_7:.2f}%.')
    print(f'Percentual da audiência do canal 10: {percentual_10:.2f}%.')

    


main()
