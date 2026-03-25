def main():
    print('Média Final')

    reprovado = 0
    aprovado = 0
    alunos = 0

    matricula = int(input('Matricula do aluno(FLAG = 0): '))
    
    while matricula != 0:
        alunos += 1
        nota_1 = int(input('Primeira nota:'))
        nota_2 = int(input('Primeira nota:'))
        nota_3 = int(input('Primeira nota:'))
        if media_final(nota_1, nota_2, nota_3) >= 7:
            aprovado += 1
        else:
            reprovado += 1
        matricula = int(input('Matricula do aluno(FLAG = 0): '))
    
    
def media_final(n1, n2, n3):
    return ((2 * n1) + (3 * n2) + (5 * n3)) / 10

main()
#incompleto