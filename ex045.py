'''
Crie um programa que faça o computador jogar Jokenpô com você.
- Pedra, papel e tesoura.
'''
import random


print('\nVamos jogar JOKENPÔ - Pedra, papel e tesoura')
print('''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            FAÇA A SUA ESCOLHA
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
0 - PEDRA
1 - PAPEL
2 - TESOURA ''')
numero = int(input('Escolha um número para jogar: '))
lista = (['PEDRA', 'PAPEL', 'TESOURA'])
jogar = random.choice([0, 1, 2])
valendo = jogar

if valendo == 0 and numero == 1:
    print('Computador escolheu Pedra, você Papel.')
    print('VOCÊ GANHOU! Papel cobri pedra.')

elif valendo == 1 and numero == 0:
    print('Computador Escolheu Papel, você Pedra.')
    print('VOCÊ PERDEU! Papel cobri pedra')

elif valendo == 1 and numero == 2:
    print('Compuatdor escoleu Papel, você Tesoura.')
    print('VOCÊ GANHOU! Tesoura corta papel.')

elif valendo == 2 and numero == 1:
    print('Computador escolheu Tesoura, você Papel.')
    print('VOCÊ PERDEU! Tesoura corta papel.')

elif valendo == 0 and numero == 2:
    print('Compuatdor escolheu Pedra, você Tesoura.')
    print('VOCÊ PERDEU! Pedra quebra tesoura.')

elif valendo == 2 and numero == 0:
    print('Computador escolheu Tesoura, você Pedra.')
    print('VOCÊ GANHOU! Pedra quebra tesoura.')

elif valendo == numero:
    print('NINGUÉM GANHOU! Jogada empatada.')

else:
    print('Opção inválida. Escolha um número de 0 a 2 .')
    print('Tente novamente')
