#Escreva um programa que execute uma função que receba um número informado no console como parâmetro e verifique se o número informado é primo ou não.
#Nota: Número primo é um número natural, maior que 1 e que não tenha outros divisores além do 1 e dele mesmo.




def numeroPrimo():
    num = int(input('Digite um número: '))
    tot = 0
    for c in range(1, num + 1):
        if num % c == 0:
            print('\033[33m', end=' ')
            tot += 1
        else:
            print('\033[31m', end=' ')
        print(c, end=' ')
    print(f'\n\033[mO número {num} foi divisível {tot} vezes')
    if tot == 2:
        print('E por isso ele é Primo!')
    else:
        print('E por ele não é Primo!')

numeroPrimo()