'''
Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.
'''

total_primo = 0   # contador
numero = int(input('\nDigite um número: '))
for contar in range(1, numero + 1):
    if numero % contar == 0:
        print('\033[33m', end=' ')
        total_primo += 1
    else:
        print('\033[31m', end=' ')
    print(contar, end=' ')
print(f'\n\033[mO número {numero} foi divisível {total_primo} vezes.')
if total_primo == 2:
    print('E por isso ele É primo PRIMO!\n')
else:
    print('E por isso ele NÃO É PRIMO!\n')
