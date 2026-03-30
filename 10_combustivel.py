def main():
    #soma do kg de combustivel, peso da carga, peso dos passageiros
    peso_decolagem = 0
    #1.5kg por l
    #quant min = 10.000 l > peso min = 15.000 kg
    combustivel = 0
    #somatorio dos containers
    peso_carga = 0
    #70kg
    
    passageiros = 0
    #10kg
    peso_container = 0
    bagagens = 0
    somatorio_bagagens = 0

    quant_containers = int(input('Insira a quantidade de containers: '))
    numeracao = 0

    while numeracao < quant_containers:
        numeracao += 1
        peso_container = float(input(f'Insira o peso do container {numeracao}: '))
        peso_carga += peso_container

    

    bilhete = int(input('Insira o número do bilhete (fim = 0):'))

    while bilhete != 0:
        passageiros += 1
        bagagens = float(input('Insira o número de bagagens: '))
        somatorio_bagagens += bagagens

        bilhete = int(input('Insira o número do bilhete (fim = 0):'))


    peso_bagagens = bagagens * 10
    peso_passageiros = passageiros * 70

    somatorio_sem_combustivel = peso_bagagens + peso_passageiros + peso_carga
    combustivel_l = (500000 - somatorio_sem_combustivel) / 1.5

    print('Resultado: ')
    print(f'Quantidade de passageiros = {passageiros}.')
    print(f'Quantidade total de volume de bagagem = {peso_bagagens}kg.')
    print(f'Peso dos passageiros: {peso_passageiros}kg.')
    print(f'Peso da carga: {peso_carga}kg.')
    print(f'Quantidade possível de combustível: {combustivel_l:.2f} litros.')

    if combustivel_l < 10000:
        print('A decolagem foi cancelada devido a falta de combustível.')
    else:
        print('A decolagem foi liberada.')
        
main()