'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor
do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguas, o aumento é de 15%.
'''


salario = float(input('Qual é o salário do funcionário: R$ '))
menor_salario = salario + (salario * 15 / 100)
maior_salario = salario + (salario * 10 / 100)

if salario <= 1250:
    print('Quem ganhava R$ {:.2f} passar a ganhar R$ {:.2f}.'.format(salario, menor_salario))
else:
    print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f}.'.format(salario, maior_salario))
