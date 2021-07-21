'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores 'M' ou 'F'. Caso esteja errada, peça a condição
novamente até ter um valor correto.
'''

m = 'm'
f = 'f'
sexo = ''

while sexo != m and sexo != f:
    sexo = str(input('\nDigite o sexo [ M / F ]: ')).lower()
    print('O sexo deve ser M ou F. Digite novamente.')
    print('-='*21)
    
print(f'O sexo digitado foi {sexo.upper()}.\n')
