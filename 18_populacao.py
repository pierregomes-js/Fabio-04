def main():

    a = 200000
    b = 300000
    cresc_a = 3.5
    cresc_b = 1.35
    anos = 0

    while a < b:
        a = a * cresc_a
        b = b * cresc_b
        anos += 1

    print(f'a = {a} habitantes.')    
    print(f'b = {b} habitantes.')
    print(f'quantidade de anospara ultrapassagem : {anos} anos.')

main()