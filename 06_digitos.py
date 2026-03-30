def main():

    n = int(input('Numero: '))
    quant_digitos = 1

    while n >= (10 ** quant_digitos):
        quant_digitos += 1
        
    print(f'QUantidade de dígitos de {n}: {quant_digitos}.')

main()