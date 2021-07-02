'''
Crie um programa que faça o computador jogar Jokenpô com você.
- Pedra, papel e tesoura.
'''
from random import randint
import time


itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('\nVamos jogar JOKENPÔ - Pedra, papel e tesoura')
print('''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            FAÇA A SUA ESCOLHA
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

if jogador >= 3:
    print('Opção inválida. Tente nbovamente.')

else:
    print('Pensando...')
    time.sleep(2)
    print('-='*11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-='*11)
    
    
    if computador == 0:
        if jogador == 0:
            print('JOGO EMPATADO.')
        elif jogador == 1:
            print('VOCÊ GANHOU!')
        elif jogador == 2:
            print('VOCÊ PERDEU.')
    
    if computador == 1:
        if jogador == 0:
            print('VOCÊ PERDEU.')
        elif jogador == 1:
            print('JOGO EMPATADO.')
        elif jogador == 2:
            print('VOCÊ GANHOU!')
    
    if computador == 2:
        if jogador == 0:
            print('VOCÊ GANHOU!')
        elif jogador == 1:
            print('VOCÊ PERDEU')
        elif jogador == 2:
            print('JOGO EMPATADO')

'''
Eu tinha feiro desta forma. A do Professor ficou com mais logica.

numero = int(input('Escolha um número para jogar: '))
lista = (['PEDRA', 'PAPEL', 'TESOURA'])
jogar = random.choice([0, 1, 2])
valendo = jogar
print('Pensando...\n')
time.sleep(2)

if valendo == 0 and numero == 1:
    print('Computador escolheu PEDRA, você PAPEL.')
    print('VOCÊ GANHOU! PAPEL cobri PEDRA.')

elif valendo == 1 and numero == 0:
    print('Computador Escolheu PAPEL, você PEDRA.')
    print('VOCÊ PERDEU! Papel cobri pedra')

elif valendo == 1 and numero == 2:
    print('Compuatdor escoleu PAPEL, você TESOURA.')
    print('VOCÊ GANHOU! Tesoura corta papel.')

elif valendo == 2 and numero == 1:
    print('Computador escolheu TESOURA, você PAPEL.')
    print('VOCÊ PERDEU! Tesoura corta papel.')

elif valendo == 0 and numero == 2:
    print('Compuatdor escolheu PEDRA, você TESOURA.')
    print('VOCÊ PERDEU! Pedra quebra tesoura.')

elif valendo == 2 and numero == 0:
    print('Computador escolheu TESOURA, você PEDRA.')
    print('VOCÊ GANHOU! Pedra quebra tesoura.')

elif valendo == numero:
    print('NINGUÉM GANHOU! Jogada empatada.')

else:
    print('Opção inválida. Escolha um número de 0 a 2 .')
    print('Tente novamente')'''
