def main():
    distancia_somatorio = 0
    litros_somatorio = 0
    
    acionar_aparelho = input('Acionar aparelho? (sim / não) : ')
    
    
    while acionar_aparelho == 'sim':
        
        if litros_somatorio > 50:
            break
        
        distancia_pecorrida = int(input('Digite a distância pecorrida em km: '))
        litros_consumidos = int(input('Digite a quantidade litros para pecorrer a distância: '))
    
        litros_somatorio += litros_consumidos
        distancia_somatorio += distancia_pecorrida
        
        acionar_aparelho = input('Acionar aparelho? (sim / não):')
            
                
        
    km_h = distancia_somatorio / litros_somatorio
    if litros_somatorio > 50:
        print('O carro parou antes do destino, devido a falta de combustível.')
    elif distancia_somatorio >= 600:
        print('O carro chegou ao seu destino. ')
    elif distancia_somatorio < 600:
        print('O carro não chegou ao seu destino. (ainda falta kilômetros).')
    print(f'Consumo em km/h do carro: {km_h:.2f}km/h .')
    
main()