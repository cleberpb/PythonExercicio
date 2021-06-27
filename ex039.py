'''
Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com a sua idade:
- Se ele ainda vai se alista ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou
passou do prazo.
'''
from datetime import date


print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
print('ALISTAMETO AO SERVIÇO MILITAR')
print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
nascimento = int(input('Qual é o seu ano de nascimento: '))
idade = date.today().year - nascimento
print('Você te {} anos.'.format(idade))
atrasado = idade - 18
falta_idade = 18 - idade

if idade <= 17:
    print('Você não tem a idade para se alistar.')
    print('Falta {} anos para o seu alistamento.'.format(falta_idade))
elif idade == 18:
    print('PARABÉNS! Você tem {} anos, já pode se alista.'.format(idade))
    print('Procure o serviço militar de sua cidade.')
elif idade >= 19:
    print('ATENÇÃO: Você está atrasado {} anos para se alista.'.format(atrasado))
    print('Procure o serviço militar de sua cidade.')
