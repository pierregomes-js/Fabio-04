def main():

    numero = int(input('Digite um número entre 0 e 255: '))


    def converter_binario(n):
        binario = ""
        numero = n
        if n == 0:
            binario = "0"
        else:
            while numero > 0:
                resto = numero % 2
                binario = str(resto) + binario
                numero //= 2
        return binario
        

    def converter_hexadecimal(n):
        hexadecimal = ""
        numero = n
        if n == 0:
            hexadecimal = "0"
        else:
            while numero > 0:
                resto = numero % 16
                if resto < 10:
                    digito = str(resto)
                else:
                    if resto == 10:
                        digito = 'A' 
                    elif resto == 11:
                        digito = 'B' 
                    elif resto == 12:
                        digito = 'C'
                    elif resto == 13:
                        digito = 'D'
                    elif resto == 14:
                        digito = 'E'
                    elif resto == 15:
                        digito = 'F'
                hexadecimal = digito + hexadecimal
                numero //= 16
        return hexadecimal
    
    numero_binario = converter_binario(numero)
    numero_hexadecimal = converter_hexadecimal(numero)

    print(f'O número {numero} em binário é {numero_binario}.')
    print(f'O número {numero} em hexadecimal é {numero_hexadecimal}.')
    

    
main()