'''
A confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria de acordo com a idade:
- Até 9 anos: MIRIM
- Atá 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Aima de 20 anos: MASTER
'''


import datetime


print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('| CONFEDERAÇÃO NACIONAL DE NATAÇÃO |')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print('Categoria de acordo com a idade')

nascimento = int(input('\nEm que ano você nasceu? '))
ano_atual = datetime.date.today().year
idade = ano_atual - nascimento

if idade <= 9:
    print('Com {} anos, sua categoria é MIRIM.'.format(idade))
elif idade == 19:
    print('Com {} anos, sua categoria é JUNIOR.'.format(idade))
elif idade == 20:
    print('Com {} anos, sua categoria é SÊNIOR.'.format(idade))
elif idade >= 21:
    print('Com {} anos, sua categoria é MASTER.'.format(idade))
else:
    print('Com {} anos, sua categoria é INFANTIL.'.format(idade))
