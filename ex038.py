'''
Escreva um programa que leia dois números inteiros
e compare-os, mostrando na tela uma mensagem:
- O primeiro é maior
- O segundo é maior
- Não existe valor maior,os dois são iguais
'''

numero01 = int(input('Digite o primeiro número: '))
numero02 = int(input('Digite o segundo número: '))

if numero01 > numero02:
    print('O primeiro número é maior.')
elif numero02 > numero01:
    print('O segundo número é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
