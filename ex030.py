'''
Crie um programa que leia um número inteiro e mostre na tela se ele é Par ou Impar.
'''

numero = int(input('Digite um número para saber se ele é Par ou Impar: '))
resultado = numero % 2

if resultado == 0:
    print('Você digitou {} e ele é PAR.'.format(numero))
else:
    print('Você digitou {} e ele é IMPAR.'.format(numero))
