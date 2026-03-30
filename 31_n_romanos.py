def main():
    def obter_unidades(n):
        return n % 10

    def obter_dezenas(n):
        return (n // 10) % 10

    def obter_centenas(n):
        return (n // 100) % 10
    
    def converter(digito, unidade, cinco, dez):

        if digito == 0:
            return ""
        elif digito <= 3:
            return unidade * digito
        elif digito == 4:
            return unidade + cinco
        elif digito == 5:
            return cinco
        elif digito <= 8:
            return cinco + unidade * (digito - 5)
        elif digito == 9:
            return unidade + dez
        
    numero = int(input('Digite um número de 1 à 999:'))

    unidade = obter_unidades(numero)
    dezena = obter_dezenas(numero)
    centena = obter_centenas(numero)

    parte_unidades = converter(unidade, 'I', 'V', 'X')
    parte_dezenas = converter(dezena, 'X', 'L', 'C')
    parte_centenas = converter(centena, 'C', 'D', 'M')

    numero_romano = parte_unidades + parte_dezenas + parte_centenas

    print(f'O número {numero} em romano é {numero_romano}.')
    





main()