def main():
    print('Placar de Pingue-Pongue')
    
    jogador_1 = 0
    jogador_2 = 0
    
    while not (jogador_1 >= 21 and jogador_1 - jogador_2 >=2) or (jogador_2 >= 21 and jogador_2 - jogador_1 >=2):
        ponto = int(input('Ganhador da partida (1 ou 2): '))
        
        if ponto == 1:
            jogador_1 += 1
        else:
            jogador_2 += 1
            
        print(f'Placar atual: {jogador_1} X {jogador_2}.')
    
    vencedor = ''
    print('Resultado:')
    if jogador_1 > jogador_2:
        vencedor = jogador_1
    else:
        vencedor = jogador_2
        
    print(f'Vencedor: {vencedor}.')
    print(f'Placar final: {jogador_1} X {jogador_2}.')
        
        
        
main()