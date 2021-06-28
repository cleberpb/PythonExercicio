'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''


valor_01 = int(input('Primeira valor: '))
valor_02 = int(input('Segundo valor: '))
valor_03 = int(input('Terceiro valor: '))

# valor moner
menor = valor_01
if valor_02 < valor_01 and valor_02 < valor_03:
    menor = valor_02
if valor_03 < valor_01 and valor_03 < valor_02:
    menor = valor_03
print('O menor valor é {}.'.format(menor))

# valor maior
maior = valor_02
if valor_01 > valor_02 and valor_01 > valor_03:
    maior = valor_01
if valor_03 > valor_01 and valor_03 > valor_02:
    maior = valor_03
print('O maior valor é {}.'.format(maior))
