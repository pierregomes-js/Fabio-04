def main():
    numerador = int(input('Numerador: '))
    denominador = int(input('Denominador: '))

    def divisao(a, b):
        quociente = 0

        resto = a

        while resto >= denominador:
            resto = resto - b
            quociente += 1

        return print(f'Resto: {resto}, quociente: {quociente}.')
    
    divisao(numerador, denominador)

main()