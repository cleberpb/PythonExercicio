'''
Crie um programa que leia uma frase qualquer e diga
se ela é um políndromo, desconsiderando os espaços.

Ex:
- APOS A SOPA
- A SACADA DA CASA
- A TORRE DA DERROTA
- O LOBO AMA O BOLO
- ANOTARAM A DATA DA MARATONA
'''

print('-='*25)
print('''Escreva uma frase, e veja se ela pode ser lida 
de trás para ferente. OBS: deve ser sem acento.''')
print('-='*25)


frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
#for letra in range(len(junto) - 1, -1, -1):
#    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um palíndromo!\n')
else:
    print('Não é um palíndromo!\n')


'''
frase = input('\nEscreva uma frase: \n').lower()
juntar = ''.join(frase.split())
print(f'Você escreveu a frase: {frase}.\n')
inverter = juntar[::-1]

if juntar == inverter:
    print(f'Está frase lida de trás para frete fica do mesmo jeito.')
    print('Ela é um Políndromo.')
else:
    print(f'Está frase lida de trás para frente fica muito doida.')
    print('Ela NÃO é um políndromo.\n')
'''
