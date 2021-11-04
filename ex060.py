'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex:
5! = 5x4x3x2x1 = 120
'''

import math


numero = 1
while numero >= 1 :
    numero = int(input('\nDigite um número inteiro: '))
    fatorial = math.factorial(numero)
    print(f'O fatorial de {numero} é {fatorial}.')
    print('-='*15)    
print('Você saiu do programa')
