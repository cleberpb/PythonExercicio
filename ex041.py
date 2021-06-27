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
