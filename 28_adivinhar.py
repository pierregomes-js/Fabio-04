import random

def main():
    print('Jogo de adivinhação')

    contador = 0
    n_sorteado = random.randint(1, 100)
    numero = int(input('Insira um número: '))

    while numero != n_sorteado:
        
        contador += 1

        print('Número errado.')

        if numero > n_sorteado:
            print('Palpite: o número sorteado é menor.')
        else:
            print('Palpite: o número sorteado é maior.')


        numero = int(input('Insira outro número: '))
    

    
        print('Parabéns, você conseguiu.')
        print(f'Quantidade de tentativas: {contador}.')
    



main()