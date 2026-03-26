def main():
    print('Pingue - Pongue')
    jogador_1 = 0
    jogador_2 = 0
    ponto = int(input('Ganhador da partida (1 - jogador 1, 2 - jogador 2): '))

    while jogador_1 < 21 or jogador_2 < 21:
        if ponto == 1:
            jogador_1 += 1
        else:
            jogador_2 += 2
        ponto = int(input('Ganhador da partida (1 - jogador 1, 2 - jogador 2): '))

    if jogador_1 - jogador_2 >= 2:
        print('Ganhador: Jogador 1')
    elif jogador_2 - jogador_1 >= 2:
        print('Ganhador: Jogador 2')
    else:
        print('Partidas finais.')


    print(f'Pontos do jogador 1: {jogador_1}.')
    print(f'Pontos do jogador 2: {jogador_2}.')



main()
#incompleo