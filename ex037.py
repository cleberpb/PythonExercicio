''' Escreva um programa que leia um número inteiro
qualquer e peça para o usuário escolher qual será
a base de conversão:
'''

print('CONVERSÃO DE NÚMEROS INTEIRO')
print('*'*42)
numero = int(input('Digite um número inteiro: '))

print('-'*42)
print('Opções para conversão:')
print('1 - Binário | 2 - Octal | 3 - Hexadecimal')
opcao = int(input('Escolha uma opçãp: '))
print('-'*42)

'''
Eu fiz este pedaço de código - está funcionando
a1 = ('{0:b}'.format(numero))
b1 = ('{:o}'.format(numero))
c1 = ('{0:x}'.format(numero))

if opcao == 1:
    print('Em Binário é {}'.format(a1))
elif opcao == 2:
    print('Em Octal é {}.'.format(b1))
elif opcao == 3:
    print('Em Hexadecimal é {}.'.format(c1))
else:
    print('\nOpção inválida! Tente novamente.')'''

if opcao == 1:
    print('{numero, bin} convertido para BINÁRIO é igual a {}.'.format((numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(numero, hex(numero)[2:]))
else:
    print('\nOpção inválida! Tente novamente.')
