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
frase = input('\nEscreva a frase: ').lower()
juntar = ''.join(frase.split())
print(f'Você escreveu a frase {frase}.')
inverter = juntar[::-1]

if juntar == inverter:
    print(f'Está frase lendo de trás para frete fica: {inverter}.')
    print('Ela é um Políndromo.')
else:
    print(f'Está frase lendo de trás para frente fica: {inverter}.')
    print('Ela NÃO é um políndromo. ')
