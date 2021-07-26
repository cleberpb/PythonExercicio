'''
Melhore o jogo do desafio 028 onde o computador vai "pensar" em um
número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessários
para vencer.
'''

import random


print('\n*************************************************************************')
print('VAMOS JOGAR? Eu vou pensar em um número de 0 a 10, e você deve adivinhar.')
print('*************************************************************************')

contador = 0
numero_chutado = 0
computaddor = ''

while numero_chutado != computaddor :
    computaddor = random.choice([1,2,3,4,5,6,7,8,9,10])    
    numero_chutado = int(input('Chute um número de 1 a 10: '))
    print(f'ERROU! Eu pensei {computaddor} e você chutou o número {numero_chutado}.')
    print('------------ Chute outro número ------------\n')
    contador += 1
    
print(f'PARABÉNS! Você chutou o número {numero_chutado} e eu pensei {computaddor}.')
print(f'Você chutou {contador} número(s).')
print('----------------- VOCÊ VENCEU -----------------\n')
    
