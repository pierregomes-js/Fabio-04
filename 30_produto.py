def main(): 
    unidade = 0
    valor = 0
    produto = input('insira o nome do produto(FLAG = fim): ')
    preco = float(input('insira o preço do produto: '))

    while produto != 'fim':
        unidade += 1
        valor += preco
        produto = input('insira o nome do produto(FLAG = fim): ')
        if produto == 'fim':
            break
        else:
            preco = float(input('insira o preço do produto: '))
        
    if unidade <= 10:
        print(f'valor = {valor}')
    elif unidade <= 20:
        print(f'valor = {valor * 0.90}')
    elif unidade <= 50:
        print(f'valor = {valor * 0.80}')
    else:
        print(f'valor = {valor * 0.75}')

main()