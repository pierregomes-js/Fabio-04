def main():
    print('Cartão 1: ')
    nome = input('Nome da candidata(flag = fim): ')
    peso = float(input('Peso da candidata: '))
    altura = float(input('altura da candidata: '))

    cartao = 1

    nome_gorda = nome
    nome_magra = nome
    peso_gorda = peso
    peso_magra = peso
    maior_altura = altura
    menor_altura = altura
    maior_altura_nome = nome
    menor_altura_nome = nome

    while nome != 'fim':
        cartao += 1
        if peso > peso_gorda:
            nome_gorda = nome
            peso_gorda = peso
        if peso < peso_magra:
            nome_magra = nome
            peso_magra = peso
        if altura > maior_altura:
            maior_altura_nome = nome
            maior_altura = altura
        if altura < menor_altura:
            menor_altura_nome = nome
            menor_altura = altura

        print(f'Cartão {cartao}:')
        nome = input('Nome da candidata(flag = fim): ')
        if nome == 'fim':
            break
        peso = float(input('Peso da candidata: '))
        altura = float(input('altura da candidata: '))
    
    print('Resultado final:')
    print(f'Nome da mais gorda e seu peso: {nome_gorda}, {peso_gorda} kg.')
    print(f'Nome da mais magra e seu peso: {nome_magra}, {peso_magra} kg.')
    print(f'Nome da mais alta e sua altura: {maior_altura_nome}, {maior_altura} cm.')
    print(f'Nome da mais baixa e sua altura: {menor_altura_nome}, {menor_altura} cm.')



main()