'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random

print('************************************************************************')
print('Vamos jogar? Eu vou pensar em um número de 0 a 5, e você deve adivinhar.')
print('************************************************************************')
numero = int(input('Digite o número que eu pensei: '))
computador = random.choice([0, 1, 2, 3, 4, 5])

if numero == computador:
    print('PARABÉNS! Você acertou. Eu pesei {}.'.format(computador))
else:
    print('Você errou! Eu pensei {}.'.format(computador))
