'''
Crie um programa que leia duas notas de um aluno e calcule
sua média, mostrando uma mensagem no final de acordo com a
média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou supoerior: APROVADO
'''

nota01 = float(input('Digite a primeira nota: '))
nota02 = float(input('Digite a segunda nota: '))
media = (nota01 + nota02) / 2

if media <= 4.9:
    print('Sua média foi {}. Você está REPROVADO.'.format(media))
elif media > 7.0:
    print('PARABÉNS! sua média foi {}. Você está APROVADO.'.format(media))
else:
    print('Sua média foi {}. Você está de RECUPERAÇÃO.'.format(media))
